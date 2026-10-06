# Third-party notices

## Compound Engineering review and simplification skills

`skills/ss-code-review/` and `skills/ss-simplify-code/` are adapted from the
Compound Engineering plugin, version 3.24.0, distributed by the
`openai-curated-remote` marketplace. Upstream repository:
https://github.com/EveryInc/compound-engineering-plugin

Local adaptations replace plugin configuration and temporary-directory paths
with steven-stack paths, remove dependencies on other Compound Engineering
skills, and use steven-stack's technical-writing skill for review prose.
Review mechanics and prompts are retained. The simplification skill is narrowed
to reuse and redundant runtime work as a delivery addon; overlapping quality
review is removed, its remaining prompts are adapted, and delivery verification
is owned by the caller. Behavior-preserving guardrails are retained. Upstream environment-variable names and plan input
contracts remain compatible.

The following upstream license applies to these adapted files:

MIT License

Copyright (c) 2025 Every

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
