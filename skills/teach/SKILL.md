---
name: teach
description: Explains what code does and why it has that design. Use for teaching requests about a change or subsystem.
disable-model-invocation: true
---

# Teach

Explain what the code does, how it works, and why it has that design. Match the depth to the person's question and let them set the pace. This skill explains the work without changing it.

Use `how` for runtime behavior and `why` for design rationale. Preserve `why`'s confidence language when combining their findings. Those qualifications describe the evidence.

## Prepare the explanation

1. Infer what the person needs to understand from the conversation. They may be reviewing a change, debugging, preparing to edit, or learning the subsystem. Skip what they already know without quizzing them.
2. Read enough code to identify the relevant area, then invoke `how` and `why` rather than repeating their investigations. Run both in parallel for a subsystem. One may suffice for a small change.
3. Keep the question for `why` narrow unless the rationale itself needs a broader search. Put the scope in the request, such as git history plus one or two sources. Let `why` record skipped categories under its own contract.

## Explain at the person's pace

Start with a plain definition and the common name, if one exists. Connect it to the current code, then explain the problem it solves and the mechanism. A user's actions, such as opening a chat or scrolling, can provide the sequence for the explanation.

Give the smallest complete answer first, usually one or two sentences, then wait for the person to respond. Add detail when they ask. In a one-shot run without a live person, deliver the explanation and put any offer of more detail at the end.

Explain the mechanism instead of listing functions and constants. Omit framing labels such as "the key insight", "at its core", and "TL;DR". Skip quizzes, announced pauses, and remarks about which part is important or difficult. Follow the person's lead on whether to continue.

## Build visuals one part at a time

Open the diff, code, or debugger when it helps explain the point. Draw when a picture is clearer than prose. A single simple point needs no figure.

For three or more interacting parts, use a short series of diagrams. Each redraws the previous diagram and adds one part. For a flow from A to B to C, show A to B, then add C, then add the return edge or next part. Put each diagram beside the explanation it supports.

Use Mermaid for flows and structures whose labels carry the meaning. For spatial ideas such as layout, overlap, scroll position, or a before-and-after view, use an available image-generation tool. Generate a marker-on-whiteboard image with short labels. Apply the same incremental sequence to generated images. Use both media when both help.

## Write the explanation

Apply **unslop**. Use plain spoken English as you would with a colleague. Preserve the detail needed to explain the mechanism and the qualifications required by `why`.

For example, "Virtualization runs in two parts, one for rendering and one for loading from disk. When an item scrolls out past the buffer, both its DOM node and its in-memory data are evicted."

Use sentence case and periods. Keep each sentence to one or two commas. Split clauses that make the sentence hard to follow. Give each concept one name. Omit metaphors, previews, mirrored phrases such as "A without B, or B without A", and generic endings such as "the rest follows". These instructions are not headings or labels to repeat in the response.

Return the explanation itself. Lead with the main point, followed by what the code is, how it works, why it has that design, and any useful questions to pursue with `how` or `why`.
