You must evaluate the quality of the model's responses to prompts.
The evaluation criteria are as follows:

<Compilation>
1-2  (Terrible) : Compilation - Does not compile
Side Effects - Contains semantic and syntactic errors
3 (Adequate) : Compilation - Code compiles without errors but may contain warnings
Side Effects - Contains syntactic errors but no semantic errors
4-5 (Excellent) : Compilation - Code compiles without any  errors or warnings
Side Effects - No semantic or syntactic errors or warnings

<Execution Output>
1-2  (Terrible) : Completeness - Output does not sufficiently answer the prompt at all.
Correctness - Output is irrelevant and incorrect.
3 (Adequate) : Completeness - Output somewhat answers the prompt but does not take into account all edge cases and constraints.
Correctness  - Output is relevant but not correct.
4-5 (Excellent) : Completeness - output fully answers the prompt and takes into consideration all edge cases and constraints.
Correctness - Output is relevant and completely correct.

<Performance>
1-2  (Terrible) : Optimization - Overall strategy is a sub-optimal method and no optimization steps taken.
Run Time - Code takes an unnecessary amount of time to run (i.e runtime exceeds 1 min on small datasets.)
3 (Adequate) : Optimization - Somewhat optimized.
Run Time - Code takes an acceptable amount of time to run.
4-5 (Excellent) : Optimization - Highly optimized.
Run Time - Code takes an expected time to run.

<Completeness - does the program do what it says it will>
1-2 (Terrible) : - The program does not cover important edge cases

- Prompt is very simple
  3 (Adequate) : - The program covers only some important edge cases
- Prompt could be improved in terms of complexity
  4-5 (Excellent) : - Code covers edge cases and full scopes of use cases discussed in prompt.
- Prompt is complex enough

Does the code do what it says it does, and does it execute things correctly.
1-2 (Terrible) : Standards - does not follow industry standards.
Language Proficiency - Does not use programming language effectively.
Simplicity - overly complicated or too simple implementation.
3 (Adequate) : Standards - mostly follows industry standards.
Language Proficiency - Uses some but not all of a programming language’s unique functionalities.
Simplicity - Slightly over-complicated or slightly over-simplified implementation.
4-5 (Excellent) : Standards - perfectly follows industry standards..
Language Proficiency - Effectively uses all of a programming language’s unique functionalities to improve implementation.
Simplicity - Exhaustivetly implementation without any over
Code takes advantage of the programming language.
Usage of appropriate APIs.
Strong usage of best-practices.

Based on these criteria, rate your model's responses to the following prompts on a scale of 1 to 5.
Sum it up and evaluate it as only one score (not 1-2 or 4-5, say only one score).
