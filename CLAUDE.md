# leetcode-solutions

LeetCode 풀이를 모아 둔 학습용 저장소다.
초보자도 읽으므로 이름과 주석의 품질이 중요하다.
새 풀이를 더하거나 기존 풀이를 다듬을 때 아래 규칙을 기본으로 적용한다.

## 답변 언어

All user-facing text in Korean (reports, progress, questions, Bash descriptions). Re-check after context compaction, where English drift recurs. Code, paths, commands, identifiers stay as-is.

## 풀이 문체

1. 주석은 한국어로 쓴다. 메서드 첫 줄에 핵심 아이디어를 적고, 다음 줄에 `# 시간 복잡도: O(...)`를 따로 적고, 비자명한 줄에만 인라인 주석을 단다.
2. 주석 한 줄은 180자까지로 보고, 180자 안이면 여러 줄로 쪼개지 않는다.
3. 코드 스멜(오타, 내장 이름 가림, 죽은 분기)과 파이썬답지 않은 이름은 고친다. 더 빠른 최적해가 있으면 그것으로 바꾼다.

## LeetCode 관례

- 메서드 이름(camelCase)과 매개변수 이름은 LeetCode가 정한 서명이므로 바꾸지 않는다. 지역 변수와 내부 헬퍼만 snake_case로 쓴다.
- `List`, `Optional`, `ListNode`, `deque` 같은 이름은 LeetCode가 미리 가져와 주므로 파일에 import를 넣지 않는다. ruff의 F821 경고는 의도한 것이다.
- `pyproject.toml`의 ruff 설정은 lint(Q000, 큰따옴표)와 format(quote-style single)이 서로 어긋난다. 따옴표는 건드리지 않는다.

## 검증

로직을 바꿀 때는 저장소 밖의 임시 폴더에 브루트포스 비교 스크립트를 두고 결과가 같은지 확인한 뒤 커밋한다.

## 커밋

커밋은 의미 단위(fix, perf, refactor, docs)로 나눈다.
메시지 형식은 아래와 같다.

One line `<type>: <message>` + `Co-Authored-By` trailer only. No body, no other footers; breaking change = `<type>!:`. Conventional Commits types; message in English, lowercase, imperative, readable without session context (no `R1`, `Phase 2`).

## 코딩 원칙

아래 원칙이 위의 풀이 문체나 LeetCode 관례와 부딪히면 풀이 규칙을 따른다.
예를 들어 3번은 멀쩡한 코드를 고치지 말라고 하지만, 풀이를 다듬는 작업에서는 코드 스멜과 이름을 고치고 더 빠른 최적해로 바꾼다.

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
