from Runner.Runner import Runner

runner = Runner(20)
print('Enter 1 For Test \nEnter 2 For just run')
isTest = input('Is it test?\n')
competitionMode = False
if isTest == '1':
    print('Enter 1 For competition \nEnter 2 For test with 20 question')
    isCompetition = input('Is it competition ? :)\n')
    if isCompetition == '1':
        competitionMode = True

    result, questionCount = runner.test(competitionMode)
    print('---------- RESULT ----------')
    if competitionMode:
        competitionMode = str(competitionMode)  + ' :)'
    print('Accuracy: ' + '% ' + str(result) + " number of questions asked: " + str(
        questionCount) + '. Is it competition: ' + str(competitionMode))
else:
    result = runner.run()
    print(result)


