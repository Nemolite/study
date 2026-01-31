a = 12
b = 'test'
console.log(`Число = ${a}, текст=   ${b}`)

//1 вариант
function myfanc(arg) {
	console.log(`Значение = ${arg}`)
}

myfanc(777)

// 2 вариант
const myfanc2 = function (arg) {
	console.log(`Значение = ${arg}`)
}
myfanc2(777)

// 3 вариант
const myfanc3 = arg => {
	console.log(`Значение = ${arg}`)
}

myfanc3('txt')

const myfanc4 = () => {
	console.log(`myfanc4`)
}

myfanc4()

function myfanc5(a, b) {
	function s(x, y) {
		return x + y
	}
	return s(a, b)
}
console.log(myfanc5(2, 3))

;(function () {
	console.log('Привет мир')
})()

function s(a) {
	su = 0
	for (let i = 0; i < arguments.length; i++) {
		su = su + arguments[i]
	}
	return su
}

numers = [1, 2, 3]
res = s(...numers) // s(1,2,3)
console.log(res)

function youSayGoodBye() {
	let s = 0
	function andISayHello(a) {
		s = s + a
		//alert(s)
		console.log(s)
	}
	return andISayHello
}

let something = youSayGoodBye()
ind = 1
for (let i = 0; i < 10; i++) {
	something(ind)
}
