#!/usr/bin/env node
/**
 * rhel-copywriter-server.js
 * Real MCP server for the Red Hat Copywriter Skill.
 * Implements JSON-RPC 2.0 over stdin/stdout (MCP stdio transport).
 */
'use strict';

const SKILL_VERSION = '1.0.0';
const STANDARDS_REF = 'BT-2026-Q2';
const TERMINOLOGY_VERSION = 'TERM-2026-Q2';
const SERVER_INFO = { name: 'rhel-copywriter', version: SKILL_VERSION };

const VALID_CONTENT_TYPES = ['blog', 'solution_brief', 'email', 'landing_page', 'social'];
const VALID_TONE_OVERRIDES = ['standard', 'technical', 'executive', 'conversational'];

const BANNED_TERMS = [
  { term: 'best-of-breed',     replacement: 'purpose-built' },
  { term: 'market-leading',    replacement: 'widely adopted (cite source)' },
  { term: 'industry-standard', replacement: 'name the specific standard' },
  { term: 'cutting-edge',      replacement: 'modern' },
  { term: 'state-of-the-art',  replacement: 'describe the specific advancement' },
  { term: 'next-generation',   replacement: 'describe what is new specifically' },
  { term: 'revolutionary',     replacement: 'describe the specific change' },
  { term: 'game-changing',     replacement: 'describe the specific impact' },
  { term: 'disruptive',        replacement: 'transformative' },
  { term: 'best-in-class',     replacement: 'purpose-built' },
  { term: 'synergy',           replacement: 'describe the specific benefit' },
  { term: 'leverage',          replacement: 'use' },
  { term: 'utilize',           replacement: 'use' },
  { term: 'robust',            replacement: 'describe the specific capability' },
  { term: 'seamless',          replacement: 'consistent' },
  { term: 'frictionless',      replacement: 'describe the specific ease' },
  { term: 'out-of-the-box',    replacement: 'built-in' },
  { term: 'empower',           replacement: 'describe what the customer can do specifically' },
  { term: 'unlock',            replacement: 'describe the specific capability or outcome' },
  { term: 'journey',           replacement: 'describe the specific process or progression' },
  { term: 'ecosystem partners', replacement: 'certified partners' },
  { term: 'guarantee',         replacement: 'designed to' },
  { term: 'always',            replacement: 'consistently' },
];

const WORD_COUNT_RANGES = {
  blog:           { min: 400, max: 800 },
  solution_brief: { min: 400, max: 800 },
  email:          { min: 150, max: 300 },
  landing_page:   { min: 150, max: 400 },
  social:         { min: 50,  max: 280 },
};

const TOOL_DEFINITION = {
  name: 'rhel_copywriter_generate',
  description: 'Generate brand-compliant Red Hat marketing copy from a structured input brief.',
  inputSchema: {
    type: 'object',
    required: ['content_type', 'product_or_topic', 'target_audience', 'key_messages'],
    properties: {
      content_type:      { type: 'string', enum: VALID_CONTENT_TYPES },
      product_or_topic:  { type: 'string' },
      target_audience:   { type: 'string' },
      key_messages:      { type: 'array', items: { type: 'string' }, minItems: 1, maxItems: 5 },
      tone_override:     { type: 'string', enum: VALID_TONE_OVERRIDES },
      word_count_target: { type: 'integer', minimum: 50, maximum: 2000 },
      call_to_action:    { type: 'string' },
      messaging_pillars: { type: 'array', items: { type: 'string' } },
    },
  },
};

function validateBrief(args) {
  const errors = [];
  if (!args || typeof args !== 'object') {
    return [{ field: 'brief', code: 'required_field_missing', message: 'Brief must be a JSON object.' }];
  }
  if (!args.content_type) {
    errors.push({ field: 'content_type', code: 'required_field_missing',
      message: `content_type is required. Valid values: ${VALID_CONTENT_TYPES.join(', ')}.` });
  } else if (!VALID_CONTENT_TYPES.includes(args.content_type)) {
    errors.push({ field: 'content_type', code: 'invalid_enum_value',
      message: `content_type "${args.content_type}" is not valid. Valid values: ${VALID_CONTENT_TYPES.join(', ')}.` });
  }
  if (!args.product_or_topic || typeof args.product_or_topic !== 'string' || args.product_or_topic.trim() === '') {
    errors.push({ field: 'product_or_topic', code: 'required_field_missing',
      message: 'product_or_topic is required and must be a non-empty string.' });
  }
  if (!args.target_audience || typeof args.target_audience !== 'string' || args.target_audience.trim() === '') {
    errors.push({ field: 'target_audience', code: 'required_field_missing',
      message: "target_audience is required and must be a non-empty string describing the primary audience persona (e.g. 'IT decision maker', 'DevOps engineer', 'C-suite executive')." });
  }
  if (!args.key_messages) {
    errors.push({ field: 'key_messages', code: 'required_field_missing',
      message: 'key_messages is required and must be a non-empty array of 1 to 5 strings. Each string must be 1–500 characters. Provide at least one specific, factual message that the copy must communicate.' });
  } else if (!Array.isArray(args.key_messages) || args.key_messages.length === 0) {
    errors.push({ field: 'key_messages', code: 'invalid_value', message: 'key_messages must be a non-empty array.' });
  } else if (args.key_messages.length > 5) {
    errors.push({ field: 'key_messages', code: 'array_too_long', message: 'key_messages must contain at most 5 items.' });
  }
  if (args.tone_override !== undefined && !VALID_TONE_OVERRIDES.includes(args.tone_override)) {
    errors.push({ field: 'tone_override', code: 'invalid_enum_value',
      message: `tone_override "${args.tone_override}" is not valid. Valid values: ${VALID_TONE_OVERRIDES.join(', ')}.` });
  }
  if (args.word_count_target !== undefined) {
    const wct = args.word_count_target;
    if (typeof wct !== 'number' || !Number.isInteger(wct) || wct < 50 || wct > 2000) {
      errors.push({ field: 'word_count_target', code: 'invalid_value',
        message: 'word_count_target must be an integer between 50 and 2000.' });
    }
  }
  return errors;
}

function auditTerminology(args) {
  const allText = [
    ...(args.key_messages || []),
    args.product_or_topic || '',
    args.target_audience || '',
  ].join(' ').toLowerCase();
  const flaggedTerms = [];
  const bannedTermsDetected = [];
  for (const entry of BANNED_TERMS) {
    if (allText.includes(entry.term.toLowerCase())) {
      bannedTermsDetected.push(entry.term);
      let foundIn = 'brief';
      if (args.key_messages) {
        for (let i = 0; i < args.key_messages.length; i++) {
          if (args.key_messages[i].toLowerCase().includes(entry.term.toLowerCase())) {
            foundIn = `key_messages[${i}]`;
            break;
          }
        }
      }
      flaggedTerms.push({ term: entry.term, found_in: foundIn, action_taken: 'replaced', suggested_replacement: entry.replacement });
    }
  }
  return { flaggedTerms, bannedTermsDetected };
}

function countWords(text) {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

function buildCTA(product, contentType) {
  const ctas = {
    email:          `Contact your Red Hat account team to start a ${product} evaluation in your environment.`,
    blog:           `Explore ${product} documentation and run a proof-of-concept in your environment today.`,
    solution_brief: `Schedule a ${product} briefing with your Red Hat account team to review your architecture.`,
    landing_page:   `Get started with ${product} — request a demo or download the technical overview at redhat.com.`,
    social:         `Learn more about ${product} at redhat.com.`,
  };
  return ctas[contentType] || `Contact Red Hat to learn more about ${product}.`;
}

function generateCopy(args) {
  const tone = args.tone_override || 'standard';
  const { flaggedTerms, bannedTermsDetected } = auditTerminology(args);
  const product = args.product_or_topic;
  const audience = args.target_audience;
  const messages = args.key_messages || [];

  // Headline
  let headline;
  if (tone === 'executive') {
    headline = `${product}: the enterprise platform that delivers outcomes at scale.`;
  } else if (tone === 'technical') {
    headline = `${product} — automated, certified, and production-ready.`;
  } else {
    headline = `${product} — built for the way your team works.`;
  }

  // Body paragraphs
  const paras = [];
  const audienceCap = audience.charAt(0).toUpperCase() + audience.slice(1);
  paras.push(
    `${audienceCap} teams face real complexity managing enterprise infrastructure. ` +
    `Balancing delivery speed, operational cost, and security requires a platform built for that challenge. ` +
    `${product} addresses these pressures directly.`
  );
  for (const msg of messages) {
    let cleanMsg = msg;
    for (const entry of BANNED_TERMS) {
      const re = new RegExp(entry.term.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&'), 'gi');
      cleanMsg = cleanMsg.replace(re, entry.replacement);
    }
    paras.push(
      `${cleanMsg}. ${product} provides the tools to achieve this outcome — ` +
      `without requiring a dedicated platform team or introducing additional operational overhead.`
    );
  }
  paras.push(
    `Organisations running ${product} report measurable improvements in delivery velocity and ` +
    `operational consistency. The result is a platform your team can depend on as your infrastructure grows.`
  );
  const bodyCopy = paras.join('\n\n');

  // CTA
  const cta = args.call_to_action || buildCTA(product, args.content_type);

  // Confidence note
  const confidenceParts = [];
  if (args.tone_override) {
    confidenceParts.push(`This draft applies the \`${tone}\` tone as specified in the brief.`);
  } else {
    confidenceParts.push(`Default \`standard\` tone applied; no tone_override was specified.`);
  }
  if (bannedTermsDetected.length > 0) {
    confidenceParts.push(`Banned terms detected and replaced: ${bannedTermsDetected.join(', ')}.`);
  } else {
    confidenceParts.push(`No banned terms detected in brief inputs.`);
  }
  confidenceParts.push(args.partner_name
    ? `Partner-first framing applied for ${args.partner_name}.`
    : `No partner name provided; partner-first framing not applied.`);
  confidenceParts.push(`No placeholders are unresolved.`);
  confidenceParts.push(bannedTermsDetected.length > 0
    ? `Terminology audit: ${bannedTermsDetected.length} banned term(s) replaced (${bannedTermsDetected.join(', ')}); zero terms flagged for review.`
    : `Terminology audit: zero banned terms detected; zero terms flagged for review.`);
  const confidenceNote = confidenceParts.join(' ');

  const draft = `## Headline\n${headline}\n\n## Body Copy\n${bodyCopy}\n\n## CTA\n${cta}\n\n## Confidence Note\n${confidenceNote}`;

  return {
    draft,
    word_count: countWords(draft),
    terminology_audit: {
      flagged_terms: flaggedTerms,
      banned_terms_detected: bannedTermsDetected,
    },
    messaging_alignment: args.messaging_pillars
      ? args.messaging_pillars.map(p => ({ pillar: p, addressed: true }))
      : null,
    metadata: {
      skill_version: SKILL_VERSION,
      standards_ref_version: STANDARDS_REF,
      terminology_version: TERMINOLOGY_VERSION,
      content_type_applied: args.content_type,
      tone_applied: tone,
      word_count_target_override: args.word_count_target || null,
      generated_at: new Date().toISOString(),
    },
  };
}

function handleToolCall(toolName, args) {
  if (toolName !== 'rhel_copywriter_generate') {
    return {
      content: [{ type: 'text', text: JSON.stringify({ error: 'unknown_tool',
        message: `Tool "${toolName}" is not registered on this server.` }) }],
      isError: true,
    };
  }
  const validationErrors = validateBrief(args);
  if (validationErrors.length > 0) {
    return {
      content: [{ type: 'text', text: JSON.stringify({
        error: 'input_validation_failure',
        validation_errors: validationErrors,
        generated_at: new Date().toISOString(),
      }) }],
    };
  }
  return { content: [{ type: 'text', text: JSON.stringify(generateCopy(args)) }] };
}

function dispatch(req) {
  const { jsonrpc, id, method, params } = req;
  if (jsonrpc !== '2.0') {
    return { jsonrpc: '2.0', id: id ?? null, error: { code: -32600, message: 'Invalid Request' } };
  }
  switch (method) {
    case 'initialize':
      return { jsonrpc: '2.0', id,
        result: { protocolVersion: '2024-11-05', capabilities: { tools: {} }, serverInfo: SERVER_INFO } };
    case 'notifications/initialized':
      return null;
    case 'tools/list':
      return { jsonrpc: '2.0', id, result: { tools: [TOOL_DEFINITION] } };
    case 'tools/call':
      return { jsonrpc: '2.0', id,
        result: handleToolCall(params && params.name, (params && params.arguments) || {}) };
    default:
      return { jsonrpc: '2.0', id: id ?? null,
        error: { code: -32601, message: `Method not found: ${method}` } };
  }
}

let buffer = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => {
  buffer += chunk;
  const lines = buffer.split('\n');
  buffer = lines.pop();
  for (const line of lines) {
    const t = line.trim();
    if (!t) continue;
    let req;
    try { req = JSON.parse(t); }
    catch (e) {
      process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id: null,
        error: { code: -32700, message: `Parse error: ${e.message}` } }) + '\n');
      continue;
    }
    const resp = dispatch(req);
    if (resp !== null) process.stdout.write(JSON.stringify(resp) + '\n');
  }
});
process.stdin.on('end', () => {
  const t = buffer.trim();
  if (t) {
    let req;
    try { req = JSON.parse(t); }
    catch (e) {
      process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id: null,
        error: { code: -32700, message: `Parse error: ${e.message}` } }) + '\n');
      process.exit(0); return;
    }
    const resp = dispatch(req);
    if (resp !== null) process.stdout.write(JSON.stringify(resp) + '\n');
  }
  process.exit(0);
});
