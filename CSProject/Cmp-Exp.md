You must evaluate the quality of the model's responses to prompts.
The evaluation criteria are as follows:

<Spelling Grammar / Languages>
1-2 (Terrible) : Readability - The response has multiple spelling or grammatical errors that significantly impact the readability - how easily the response can be parsed by human readers
Language Mechanics - Response includes errors that may encompass incorrect verb forms, sentence structure problems, run-on sentences, punctuation and sentence fragments
3 (Adequate) : Readability - The response has some spelling or grammatical errors but the response is still readable
Language Mechanics - Response indicates proficient use of language mechanics, with only minor corrections
4-5 (Excellent) : Readability - The response has no spelling or grammatical errors
Language Mechanics - Response indicates advanced use of language mechanics, with no minor corrections

<Code Documentation>
1-2  (Terrible) : Code/In-line Documentation - no in-line documentation
3 (Adequate) : Code/In-line Documentation - Variable names are accurate.
Comments all over the code.
Lack of docstrings.
4-5 (Excellent) : Code/In-line Documentation - Variable names are accurate.
Code contains a reasonable amount of helpful inline comments

<Overall Helpfulness>
1-2  (Terrible) : Accuracy - The non code explanation is not accurate OR missing
Helpfulness - The non code explanation is unhelpful or barely helpful OR missing.
3 (Adequate) : Accuracy -  The non code explanation of the answer is somewhat understood and accounted for.
Helpfulness - The non code explanation is somewhat helpful.
4-5 (Excellent) : Accuracy - The non code explanation of the answer is fully understood and accounted for.
Helpfulness - The non code explanation of the answer entirely answers the prompt.

<Tone Appropriateness>
1-2  (Terrible) : The prompt and response do not use the right tone for the context of the task type (formal, informal, amount of technical jargon)
3 (Adequate) : The tone of the prompt and response is hit or miss
4-5 (Excellent) : The prompt and response use the right tone for the context of the task type (formal, informal, amount of technical jargon)

<Explanation Depth>
1-2  (Terrible) : Depth - The non code explanation does not go into enough detail OR missing
3 (Adequate) : Depth -  The non code explanation goes into some detail but falls short with implicit requests or caveats.
4-5 (Excellent) : Depth The non-code portion of the text explains the problem, context and solution to a sufficient degree of depth, the user should completely understand the solution with this response

Based on these criteria, rate your model's responses to the following prompts from 1 to 5.
Combine them and output them as only one score.
