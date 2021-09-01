@serializable
class APIPayload {
  getValue(): Payload {
    // ...
  }
}
// wraps pay load class and optionally returns a new class and replaces it

// equiv too

let APIPayload = serializable(class APIPayload {
    getValue(): Payload {
      // ...
    }
  })

