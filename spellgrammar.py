import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
# text = ["wht posible way to kno the walue of indexxing serch n how to improve it's algortms",
#         "howw kan i deletete filz frm windows 10",
#         "i have benn done my job sinc the past elevin yrs and it tuk me lot of corage to finis wurk @ the rite time",
#         "Us hav been buzi with other progects so we cudnt finish it becoz of time constrants",
#         "howw do i unistal updates dat are redundent and savy and wudnt compete when tey r rekuired",
#         "the film prodused bye mi ws not for childrun but for the ages b/w 12 and 16 teenz onli",
#         "custom suport iz best handeled by nataral proceses and acording to relevent noledge",
#         "Slack has much feetures but i ws luking for some thing simpler and more cuter than it",
#         "It iz my duti to giv dis way becoz i thunk that tis can improff hour work",
#         "Last but no leest; i would rather u use the best tool n customise it if that is neded",]


# for i in text:
#     correct = tool.correct(i)
#     print(correct)

text = input("Enter text \n")

matches = tool.check(text)

my_mistakes = []
my_corrections = []
start_positions = []
end_positions = []

for rules in matches:
    if len(rules.replacements) > 0:
        start_positions.append(rules.offset)
        end_positions.append(rules.errorLength + rules.offset)
        my_mistakes.append(text[rules.offset:rules.errorLength + rules.offset])
        my_corrections.append(rules.replacements[0])

my_new_text = list(text)

for m in range(len(start_positions)):
    for i in range(len(text)):
        my_new_text[start_positions[m]] = my_corrections[m]
        if (i > start_positions[m] and i < end_positions[m]):
            my_new_text[i] = ""

my_new_text = "".join(my_new_text)

print(my_new_text)
