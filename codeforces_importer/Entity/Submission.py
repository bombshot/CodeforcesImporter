class Submission:
    def __init__(self, id=None, contest_id=None, problem=None, verdict=None):
        self.id = id
        self.contest_id = contest_id
        self.problem = problem
        self.verdict = verdict

    def set_id(self, id):
        self.id = id;

    def set_contest_id(self, contest_id):
        self.contest_id = contest_id

    def set_problem(self, problem):
        self.problem = problem

    def set_verdict(self, verdict):
        self.verdict = verdict


def log_submission(submission):
    print "[",
    print 'id = ' + str(submission.contest_id) + submission.problem.index + ', ',
    print 'name = ' + submission.problem.name + ', ',
    print 'verdict = ' + submission.verdict + ', ',
    print 'submission_id=' + str(submission.id),
    print "]"