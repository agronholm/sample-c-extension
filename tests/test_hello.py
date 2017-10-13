from hello import say_hello_to


def test_say_hello_to(capsys):
    say_hello_to('me')
    out, err = capsys.readouterr()
    assert out == 'Hello me!\n'
