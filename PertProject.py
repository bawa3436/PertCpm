
class Project(object):

    def __init__(self,activities):
        if activities is None:
            self.activities = {}
        else:
            self.activities = activities

    def validate_graph(self):
        # TODO  '''at - implement validation of the project graph'''
        raise NotImplementedError

    def critical_path(self):
        # TODO  '''at - implement calculation of critical path'''
        raise NotImplementedError

    def add_activity(self):
        # TODO  '''at - implement add activity'''
        raise NotImplementedError

    def remove_activity(self):
        # TODO  '''at - implement raise activity'''
        raise NotImplementedError

    def find_isolated_activity(self):
        # TODO  '''at - implement find isolated'''
        raise NotImplementedError

    def show_activities_slack(self):
        # TODO  '''at - show_activities_slack - slack should be calculated in each activity at
        # creation(contructor) or in a different method and should be added as a
        # data member in runtime '''
        raise NotImplementedError

    def __str__(self):
        # TODO at - override __str__
        raise NotImplementedError


class Activity(object):

    # TODO at - maybe change c'tor and add more
    # data members like es, fs, preceding and seceding activities
    def __init__(self, name, duration):
        self.duration = duration
        self.name = name

    def __str__(self):
        # TODO at - override __str__
        raise NotImplementedError


