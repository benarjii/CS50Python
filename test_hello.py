from hello import hello

def main():
	test_default()
	test_argument()

def test_default():
	assert hello() == "hello, world"

def test_argument():
	assert hello("Ben") == "hello, Ben"

main()