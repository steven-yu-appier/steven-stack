# Verify UI with intercepted API responses

Use when an API is unreachable or its deployment lacks the required response
fields or states. Keep the actual app, routing, components and user interactions;
change only the responses needed for the confirmed scenario. An intercepted run
verifies frontend behavior, not backend permission enforcement or persistence.

## Select the interception tool

Inspect the preview's Network panel and the repository's API client first.
Identify the exact origin, method, pathname, query/body discriminator and JSON
envelope. Install the override before the request that populates the UI or user
context, then reload or refetch. Preserve unrelated calls and response fields.

- For a deployed preview in an authenticated Chrome session, prefer the existing
  Chrome/CDP harness's response interception, or Playwright routing when the host
  supports it. CDP Fetch at the response stage preserves the real request and
  replaces its response. Resume every paused request and disable interception
  on cleanup. Use a dedicated task tab/context; avoid a global profile override.
- With Playwright, use an exact request predicate, `route.fetch()` followed by
  `route.fulfill({ response, json })` for a reachable but outdated API. For an
  unreachable API, fulfill a contract-backed response with the intended status,
  headers and JSON body. Fetch through only once; retrying a write can duplicate
  its backend effect. Browser-context routes can catch requests before page boot.
- Chrome DevTools Local Overrides suit manual, stable URL responses. Track query
  variants, preflight/CORS and override indicators; disable/remove the task's
  overrides afterwards. Do not assume replacing a body repairs failed transport.
- Reuse MSW when the app already has a working worker and handlers. Do not add
  MSW to a deployed preview solely for this verification: worker hosting and
  scope require app integration. Service-worker responses can bypass Playwright
  routes; use the existing worker or a clean isolated context with workers
  blocked, and disclose that difference.

If the host exposes only read-only browser inspection, it cannot provide response
interception. Use an available supported harness, or report that capability
pending. Never present a planned override as an executed test.

## Exercise the intended scenario

1. Ground replacement data in the confirmed API contract and real response shape.
   Patch the minimal permission or data fields; keep unknown fields unchanged.
   If the new contract is unresolved, report the ambiguity instead of inventing it.
2. Restrict the handler to the scenario's exact requests. Record method, endpoint,
   original status and changed field/value pairs without tokens or auth headers.
3. Reload/refetch and confirm both that the handler matched and that the UI consumed
   the replacement. Exercise the allowed and denied states, or relevant boundary
   values, through actual controls. DOM or React-store edits are not API coverage.
4. Intercept dependent mutation responses as well when using synthetic roles or
   records. Do not send real writes under a simulated permission state. A mocked
   save/reopen demonstrates FE behavior only; real persistence remains pending.
5. Remove task-owned handlers/overrides, resume paused requests and restore normal
   responses. Keep evidence and the precise override description with the verdict.

Historical screenshots may inform a scenario but do not replace this fresh run.
If login, preview access or the required role cannot be reproduced, state the
remaining gap. A fabricated user-info response does not establish a real role's
server authorization.

## Appier preview observations

Investigated on 2026-11-18:

- iDash Campaign Rules preview under `/pr/<branch>/campaign-rules/` loads its real
  UI and fetches user context from `https://be.idash-staging.appier.org/read/userInfo`.
  The shared `idash-user-info` client supplies roles and permissions. Override
  before initial context loading; discover feature endpoints from Network.
- Portal's `/preview/develop#/aibid/<id>/report` loads the real app and may redirect
  to login. Its source uses fetch with `Authorization` and `/oauth/user_info`,
  with the API base selected by the build. Discover the deployed API origin;
  do not assume the preview hostname is the backend or copy iDash's envelope.
  This investigation stopped during login with an `access_token` loading error;
  response interception on Portal was not exercised.

Prefer response-level interception for these existing deployed apps. Recheck
runtime requests and the current contract for each task; these observations
are not universal endpoint mappings or proof of a completed intercepted run.

References: [Playwright network](https://playwright.dev/docs/network),
[CDP Fetch](https://chromedevtools.github.io/devtools-protocol/tot/Fetch/),
[Chrome Local Overrides](https://developer.chrome.com/docs/devtools/overrides/).
