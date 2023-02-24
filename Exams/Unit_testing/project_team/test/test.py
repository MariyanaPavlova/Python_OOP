from project_team.team import Team

from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test_init(self):
        team_name = 'Team'
        team = Team(team_name)

        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_raises(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("123teamASD,$%")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        self.team.members['ivam'] = 18

        result = self.team.add_member(ivam=18, pesho=21, gosho=22,)
        self.assertEqual("Successfully added: pesho, gosho", result)
        self.assertEqual(21, self.team.members['pesho'])
        self.assertEqual(21, self.team.members['pesho'])


    def test_remove_member(self):
        self.team.members['ivam'] = 18

        result = self.team.remove_member('ivam')
        self.assertEqual("Member ivam removed",result)
        self.assertEqual({}, self.team.members)

    def test_remove_member_1(self):
        self.team.members = {'ivam':18, 'gosho':20}

        result = self.team.remove_member('gogg')
        self.assertEqual("Member with name gogg does not exist", result)
        self.assertTrue('gogg' not in self.team.members)

    def test_gt_(self):
        team_one = Team("First")
        team_one.members['Ivan'] = 18
        team_one.members['Gogo'] = 21
        team_one.members['Pepi'] = 22

        team_two = Team("Second")
        team_two.members['Petko'] = 18
        team_two.members['George'] = 21

        self.assertEqual(True, team_one.__gt__(team_two))
        self.assertEqual(False, team_two.__gt__(team_one))

    def test_len_(self):
        self.team.members = {'ivam': 18, 'gosho': 20}

        self.assertEqual(2, self.team.__len__())

    def test_add_(self):
        team_one = Team("First")
        team_one.members['Ivan'] = 18

        team_two = Team("Second")
        team_two.members['Petko'] = 18
        team_two.members['George'] = 21

        new_team = team_one.__add__(team_two)

        self.assertEqual('FirstSecond', new_team.name)
        self.assertEqual({'Ivan':18, 'Petko':18, 'George':21}, new_team.members)

    def test_str_(self):
        team_one = Team("First")
        team_one.members = {'gosho':22, 'pesho':21,'ivam':18}

        result = f'Team name: First\n' \
                 f'Member: gosho - 22-years old\n'\
                 f'Member: pesho - 21-years old\n'\
                 f"Member: ivam - 18-years old"

        self.assertEqual(result, team_one.__str__())


if __name__ == "__main__":
    main()
