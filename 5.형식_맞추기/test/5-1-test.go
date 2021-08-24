package test

import "fmt"

type Something struct {
	some  string
	thing string
}

func NewSomething(some string, thing string) *Something {
	s := Something{
		some:  some,
		thing: thing,
	}
	return &s
}

func (s *Something) Some() string {
	return s.some
}

func (s *Something) Thing() string {
	return s.thing
}

func (s *Something) DoThing() {
	fmt.Println("Do " + s.thing)
}

func (s *Something) DoAnyThing() {
	ThingThingThing(s)
}

func ThingThingThing(s *Something) {
	for i := 0; i < 3; i++ {
		fmt.Println(s.Thing())
	}
}
