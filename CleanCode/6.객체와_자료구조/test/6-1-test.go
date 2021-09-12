package test

import (
	"math"
)

type Point struct {
	x float32
	y float32
}

type Figure interface {
	GetArea() float32
}

type Sqaure struct {
	point *Point
	side  float32
}

type Rectangle struct {
	point  *Point
	width  float32
	height float32
}

type Circle struct {
	point  *Point
	radius float32
}

func (s *Sqaure) GetArea() float32 {
	return s.side * s.side
}

func (r *Rectangle) GetArea() float32 {
	return r.width * r.height
}

func (c *Circle) GetArea() float32 {
	return math.Pi * c.radius * c.radius
}
