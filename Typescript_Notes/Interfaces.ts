// Type alias and interfaces are basically two ways of saying same thing

type Sushi = {
    calories: number
    salty: boolean
    tasty: boolean
  }

interface Sushi {
calories: number
salty: boolean
tasty: boolean
}

type Food = {
calories: number
tasty: boolean
}
type Sushi = Food & {
salty: boolean
}
type Cake = Food & {
sweet: boolean
}

interface Food {
calories: number
tasty: boolean
}
interface Sushi extends Food {
salty: boolean
}
interface Cake extends Food {
sweet: boolean
}

// Differences?
// type aliases are more general

type A = number
type B = A | string

// When tyou extend an interface ts will make sure that interface is assignable to your 
// extension

// ** WRONG
interface A {
    good(x: number): string
    bad(x: number): string
  }
  
  interface B extends A {
    good(x: string | number): string
    bad(x: string): string  // Error TS2430: Interface 'B' incorrectly extends
  }  

// Decleration Merging
// Interfaces in same scope are auto merged, type aliases wit hthe same name will result in a compile error

interface Animal {
    eat(food: string): void
    sleep(hours: number): void
}

interface Feline {
    meow(): void
}

class Cat implements Animal, Feline {
    eat(food: string) {
        console.log(food)
    }
    sleep(hours: number) {
        console.log(hours)
    }

    meow() {
        console.log('Meow')
    }
}

// Interfaces more light weight then abstract classes. Interface allows you to model
// a shape while abstract class can only model a class.
// When an implementation is shared amout multiple classes use an abstract class, when you need a lightweight way to say  this class is a T use an interface

// Classes are structurly typed, TS compares classes by structure not by name like nominaly typed languages

class Zebra {
    trot() {
      // ...
    }
  }
  
  class Poodle {
    trot() {
      // ...
    }
  }
  
  function ambleAround(animal: Zebra) {
    animal.trot()
  }
  
  let zebra = new Zebra
  let poodle = new Poodle
  
  ambleAround(zebra)   // OK
  ambleAround(poodle)  // OK

  // String Database

  type State = {
    [key: string]: string
  }
  
  class StringDatabase {
    //state: State = {}
    constructor(public state: State = {}) {}
    get(key: string): string | null {
      return key in this.state ? this.state[key] : null
    }
    set(key: string, value: string): void {
      this.state[key] = value
    }
    static from(state: State) {
      let db = new StringDatabase
      for (let key in state) {
        db.set(key, state[key])
      }
      return db
    }
  }

  // Generates these types
  interface StringDatabase {
    state: State
    get(key: string): string | null
    set(key: string, value: string): void
  }



// Generics  to classess

class MyMap<K, V> { 
    constructor(initialKey: K, initialValue: V) { 
      // ...
    }
    get(key: K): V { 
      // ...
    }
    set(key: K, value: V): void {
      // ...
    }
    merge<K1, V1>(map: MyMap<K1, V1>): MyMap<K | K1, V | V1> { 
      // ...
    }
    static of<K, V>(k: K, v: V): MyMap<K, V> { 
      // ...
    }
  }

// Generics to interfaces
interface MyMap<K, V> {
    get(key: K): V
    set(key: K, value: V): void
  }
