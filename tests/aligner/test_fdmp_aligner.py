from pathlib import Path
from CommonSpell.aligners.fdmp import FDMPaligner




def test_fdmp_aligner():

    token_strings = [
        '+,-.+,/0',
        '+,1.+,/0',
        '+,1.+,/0'
    ]
    token_lists = [
        [(0, 4, 1, 'བཀྲ་'), (4, 8, 1, 'ཤིས་'), (8, 12, 1, 'ཀུན་'), (12, 16, 1, 'གྱི་'), (16, 20, 1, 'བཀྲ་'), (20, 24, 1, 'ཤིས་'), (24, 25, 1, 'པ'), (25, 26, 1, '།')],
        [(0, 4, 1, 'བཀྲ་'), (4, 8, 1, 'ཤིས་'), (8, 12, 1, 'ཀུད་'), (12, 16, 1, 'གྱི་'), (16, 20, 1, 'བཀྲ་'), (20, 24, 1, 'ཤིས་'), (24, 25, 1, 'པ'), (25, 26, 1, '།')],
        [(0, 4, 1, 'བཀྲ་'), (4, 8, 1, 'ཤིས་'), (8, 12, 1, 'ཀུན་'), (12, 16, 1, 'ཀྱི་'), (16, 20, 1, 'བཀྲ་'), (20, 24, 1, 'ཤིས་'), (24, 25, 1, 'པ'), (25, 26, 1, '།')]
    ]

    expected_matrix = [
        [(0, 4, 1, 'བཀྲ་'),(0, 4, 1, 'བཀྲ་'),(0, 4, 1, 'བཀྲ་'),],
        [(4, 8, 1, 'ཤིས་'),(4, 8, 1, 'ཤིས་'),(4, 8, 1, 'ཤིས་'),],
        [(8, 16, 1, 'ཀུན་གྱི་'),(8, 16, 1, 'ཀུད་གྱི་'),(8, 16, 1, 'ཀུན་ཀྱི་'),],
        [(16, 20, 1, 'བཀྲ་'),(16, 20, 1, 'བཀྲ་'),(16, 20, 1, 'བཀྲ་'),],
        [(20, 24, 1, 'ཤིས་'),(20, 24, 1, 'ཤིས་'),(20, 24, 1, 'ཤིས་'),],
        [(24, 25, 1, 'པ'),(24, 25, 1, 'པ'),(24, 25, 1, 'པ'),],
        [(25, 26, 1, '།'), (25, 26, 1, '།'), (25, 26, 1, '།')]

    ]

    aligner = FDMPaligner()
    token_matrix = aligner.get_alignment_matrix(token_strings, token_lists)
    assert expected_matrix == token_matrix
    

test_fdmp_aligner()
