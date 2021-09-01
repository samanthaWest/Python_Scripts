// Exhaustive checking

type Weekday = 'Mon' | 'Tue'| 'Wed' | 'Thu' | 'Fri'
type Day = Weekday | 'Sat' | 'Sun'

function getNextDay(w: Weekday): Day {
  switch (w) {
    case 'Mon': return 'Tue' // Will throw an error , need to cover more cases
  }
}

// Type Operators | and & but also keying in operator

type FriendList = {
  count: number
  friends: {
    firstName: string
    lastName: string
  }[]
}

type APIResponse = {
  user: {
    userId: string
    friendList: FriendList
  }
}


function getAPIResponse(): Promise<APIResponse> {
  // ...
}

function renderFriendList(friendList: FriendList) {
  // ...
}

let response = await getAPIResponse()
renderFriendList(response.user.friendList)


// Sometimes we dont always want to come up with name for
// each top level top expecilly 
// if its generated with a gbuld tool . Instead you can key into your type

type APIResponse = {
  user: {
    userId: string
    friendList: {
      count: number
      friends: {
        firstName: string
        lastName: string
      }[]
    }
  }
}

// you can key into ay shaoe and any array i.e an individual friend
// type Friend = FriendList['friends'][number]
// number is a way to key into an array tyoe to represent the index
// you want to key into. Use br
type FriendList = APIResponse['user']['friendList']

function renderFriendList(friendList: FriendList) {
  // ...
}

// KeyOf Operator
// To get objects keys as a union of string literal types

type ResponseKeys = keyof APIResponse // 'user'
type UserKeys = keyof APIResponse['user'] // 'userId' | 'friendList'
type FriendListKeys =
  keyof APIResponse['user']['friendList'] // 'count' | 'friends'

// Combing keying in and key of operators you can implement
// typesafe getter function that looks up the value at the given key in an object

function get<O extends object, K extends keyof O> (o: O, k: K): O[K] {
  return o[k]
}

type ActivityLog = {
  lastEvent: Date
  events: {
    id: string
    type: 'Read' | 'Write'
  }[]
}

let activityLog: ActivityLog = { }
let lastEvent = get(activityLog, 'lastEvent')

// The Record Type
// Describe obj as a map something to something

type Weekday = 'Mon' | 'Tue'| 'Wed' | 'Thu' | 'Fri'
type Day = Weekday | 'Sat' | 'Sun'

let nextDay: Record<Weekday, Day> = {
  Mon: 'Tue'
}

// Mapped Types
// Alternative to Record types is Mapped Types
// Next day is an object wit a key for each week day whose value is Day

let nextDay: {[K in Weekday]: Day} = {
  Mon: 'Tue'
}

// Error TS2739: Type '{Mon: "Tue"}' is missing the following properties
// from type '{Mon: Weekday; Tue: Weekday; Wed: Weekday; Thu: Weekday;
// Fri: Weekday}': Tue, Wed, Thu, Fri.

// At most one mapped type per object

type Account = {
  id: number
  isEmployee: boolean
  notes: string[]
}

// Make all fields optional
type OptionalAccount = {
  [K in keyof Account]?: Account[K] 1
}

// Make all fields nullable
type NullableAccount = {
  [K in keyof Account]: Account[K] | null 2
}

// Make all fields read-only
type ReadonlyAccount = {
  readonly [K in keyof Account]: Account[K] 3
}

// Make all fields writable again (equivalent to Account)
type Account2 = {
  -readonly [K in keyof ReadonlyAccount]: Account[K] 4
}

// Make all fields required again (equivalent to Account)
type Account3 = {
  [K in keyof OptionalAccount]-?: Account[K] 5
}

// 1
// We create a new object type OptionalAccount by mapping over Account, marking each field as optional along the way.

// 2
// We create a new object type NullableAccount by mapping over Account, adding null as a possible value for each field along the way.

// 3
// We create a new object type ReadonlyAccount by taking Account and making each of its fields read-only (that is, readable but not writable).

// 4
// We can mark fields as optional (?) or readonly, and we can also unmark them. With the minus (–) operator—a special type operator only available with mapped types—we can undo ? and readonly, making fields required and writable again, respectively. Here we create a new object type Account2, equivalent to our Account type, by mapping over ReadonlyAccount and removing the readonly modifier with the minus (–) operator.

// 5
// We create a new object type Account3, equivalent to our original Account type, by mapping over OptionalAccount and removing the optional (?) operator with the minus (–) operator.

// Built in mapped types
// Record <Keys, Values>

// Companion Object Pattern, way to pair classes 
// and objects together comes from Scala.

type Currency = {
  unit: 'EUR' | 'GBP' | 'JPY' | 'USD'
  value: number
}

let Currency = {
  DEFAULT: 'USD',
  from(value: number, unit = Currency.DEFAULT): Currency {
    return {unit, value}
  }
}

import {Currency} from './Currency'

let amountDue: Currency = { 
  unit: 'JPY',
  value: 83733.10
}

let otherAmountDue = Currency.from(330, 'EUR') 

// Use companion obj pattern when obj and type
// are semantically related with obj providing util methods
// that operate on the type


