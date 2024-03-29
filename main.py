from Runner.RunnerFuzzy import RunnerFuzzy
from Runner.RunnerKeyword import RunnerKeyword
from SentheticDialogGeneration.Generator import Generator

runnerFuzzy = RunnerFuzzy(20)
runnerKeyword = RunnerKeyword()

print('Enter 1 For Test \nEnter 2 For Run \n Enter 3 for Senthetic Dialog Generation')
isTest = input('Is it test?\n')
competitionMode = False
if isTest == '1':
    print('Enter 1 For Fuzzy Method \nEnter 2 For Keyword Method')
    competitionMode = True
    isFuzzy = input('Enter your choose ? \n')
    print('---------- RESULT ----------')
    if isFuzzy == '1':
        result, questionCount = runnerFuzzy.test(competitionMode)
        print('Accuracy: ' + '% ' + str(result) + " number of questions asked: " + str(
            questionCount))

    else:

        result, questionCount = runnerKeyword.test()
        print('Accuracy: ' + '% ' + str(result) + " number of questions asked: " + str(
            questionCount))

elif isTest == '2':
    print('Enter 1 For Fuzzy Method \nEnter 2 For Keyword Method')
    isFuzzy = input('Enter your choose ? \n')
    if(isFuzzy == '1'):
        result = runnerFuzzy.run()
    else:
        result = runnerKeyword.run()
    print(result)
else:
    generator = Generator()
    generator.consult()

