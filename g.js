let voin1 = {
	hel: 100,
	self_hit: function (u) {
		this.hel = this.hel - u
	},
	hit: function () {
		r = Math.floor(Math.random() * (10 - 5 + 1)) + 5
		return r
	},
}

let voin2 = {
	hel: 100,
	self_hit: function (u) {
		this.hel = this.hel - u
	},

	hit: function () {
		r = Math.floor(Math.random() * (10 - 5 + 1)) + 5
		return r
	},
}

// эпизод =битва=

voin2.self_hit(voin1.hit())
voin1.self_hit(voin2.hit())

console.log('Здоровье 2 воина =' + voin2.hel)
console.log('Здоровье 1 воина =' + voin1.hel)

// while true {

// }
