from main import A, B, C, D
import getopt, sys


def run_checks_class_A():
	a = A() 
	assert(a.X == "Class A atribute X")


def run_checks_class_B():
	b = B()
	assert(b.X == "Class A atribute X")
	assert(b.Y == "Class B atribute Y extend class A")


def run_checks_class_C():
	c = C()
	assert(c.X == "Class A atribute X")	
	assert(c.Z == "Class C atribute Z extend class A")


def run_checks_class_D():
	d = D()
	assert(d.X == "Class A atribute X")	
	assert(d.Y == "Class B atribute Y extend class A")
	assert(d.Z == "Class C atribute Z extend class A")

	


def invoke_test(test):
    return {
		"-a" : run_checks_class_A,
		"-b" : run_checks_class_B,
		"-c" : run_checks_class_C,
		"-d" : run_checks_class_D,	
	}[test]()


def run_checks():	

	args, _ = getopt.getopt(sys.argv[1:], "abcd", [])
		
	if args:
		for o, _ in args: 						
			invoke_test(o)
	else:	
		print("Tipo de teste não infomado.")


run_checks()

