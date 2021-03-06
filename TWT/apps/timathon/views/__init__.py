from .home import HomeView
from .create_team import Create_team
from .view_team import View_teams
from .submission_view import Submission_View
from .add_member_view import AddMember
from .leave_member_view import LeaveTeam
from .submission_list_view import SubmissionListView
from .unvote import UnVote
from .vote import Vote
home = HomeView.as_view()
create_team = Create_team.as_view()
view_teams = View_teams.as_view()
submission = Submission_View.as_view()
add_member = AddMember.as_view()
leave_team = LeaveTeam.as_view()
submission_list = SubmissionListView.as_view()
vote = Vote.as_view()
unvote = UnVote.as_view()
