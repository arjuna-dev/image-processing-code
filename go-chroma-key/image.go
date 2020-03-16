//https://blog.golang.org/go-image-package

package main

import (
	"fmt"
	"image/jpeg"
	"image/color"
	"image/draw"
	"image"
	"os"
)

func getMax(r, g, b float32) (string, float32) {
	var val float32
	var max string
	if r>g && r>b {
		max = "red"
		val = r
	}
	if g>r && g>b {
		max = "green"
		val = g
	}
	if b>g && b>r {
		max = "blue"
		val = b
	}
	return max, val
}

func getMin(r, g, b float32) (string, float32) {
	var val float32
	var min string
	if r<g && r<b {
		min = "red"
		val = r
	}
	if g<r && g<b {
		min = "green"
		val = g
	}
	if b<g && b<r {
		min = "blue"
		val = b
	}
	return min, val
}

func getHue(r float32, g float32, b float32, max string, maxVal float32, minVal float32) float32 {
	var hue float32
	if max == "red"{
		hue = (g-b)/(maxVal-minVal)
	} else if max == "green"{
		hue = 2 + (b-r)/(maxVal-minVal)
	} else if max == "blue"{
		hue = 4 + (r-g)/(maxVal-minVal)
	}
	return hue*60
}

func changeHue(r float32, g float32, b float32, max string, maxVal float32, minVal float32, newHue float32) (newr,newg,newb uint8) {
	var r2,g2,b2 float32
	newHue = newHue/360.0
	if max == "red"{
		g2 = (newHue * (maxVal-minVal)) + b
		b2 = (newHue * (minVal-maxVal)) + g
		r2 = r
	} else if max == "green"{
		b2 = -1*(newHue-2)*minVal+(newHue-2)*maxVal+r
		r2 = b+(newHue-2)*(minVal-maxVal)
		g2 =g
	} else if max == "blue"{
		r2 = g-(newHue-4)*(minVal-maxVal)
		g2 = (newHue-4)*minVal-(newHue-4)*maxVal+r
		b2 = b
	}
	r3 := uint8(r2*255)
	g3 := uint8(g2*255)
	b3 := uint8(b2*255)
	return r3,g3,b3
}

func main() {

	f, err := os.Open("darth.jpg")
	if err != nil {
		fmt.Print("error", err)
	}
	defer f.Close()

	img, fmtName, err := image.Decode(f)
	if err != nil {
		fmt.Print(fmtName, err)
	}

	b := img.Bounds()
	m := image.NewRGBA(image.Rect(0, 0, b.Dx(), b.Dy()))
	draw.Draw(m, m.Bounds(), img, b.Min, draw.Src)

	for y := b.Min.Y; y < b.Max.Y; y++ {
		for x := b.Min.X; x < b.Max.X; x++ {
			r, g, b, _ := m.At(x, y).RGBA()
			r2 := float32(r)/65535.0
			g2 := float32(g)/65535.0
			b2 := float32(b)/65535.0
			max, maxVal := getMax(r2,g2,b2)
			_, minVal := getMin(r2,g2,b2)
			
			hue := getHue(r2, g2, b2, max, maxVal, minVal)

			if hue>110.0 && hue<125.0{
				red, green, blue := changeHue(r2, g2 ,b2, max, maxVal, minVal, 360.0)
				m.Set(x, y, color.RGBA{red, green, blue, 255})
			}
		}
	}
	
	f2, err := os.Create("outimage.jpg")
	if err != nil {
		fmt.Print("error", err)
	}
	defer f2.Close()

	// Specify the quality, between 0-100
	opt := jpeg.Options{
		Quality: 90,
	}
	err = jpeg.Encode(f2, m, &opt)
	if err != nil {
		fmt.Print("error", err)
	}
}

