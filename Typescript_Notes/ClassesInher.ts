// Build a chess engine, will model a game of chess and provide an API for two players
// to take turns making moves

// Represents a chess game
class Game {}

// A chess peice
// class Piece {}

// A set of coordinates for a peice
// class Position {}

// Peices
// Every peice has a color and current position
// class King extends Piece {}
// class Queen extends Piece {}
// class Bishop extends Piece {}
// class Knight extends Piece {}
// class Rook extends Piece {}
// class Pawn extends Piece {}

type Color = 'Black' | 'White'
type Filee = 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H'
type Rank = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8

class Position {
    constructor(
        private file: File,
        private rank: Rank
    ) {}

    distanceFrom(position: Position) {
        return {
          rank: Math.abs(position.rank - this.rank),
          file: Math.abs(position.file.charCodeAt(0) - this.file.charCodeAt(0))
        }
      }
} 

// Cant instnatiate class directly but you can define methods on it
abstract class Piece {
    protected position: Position
    constructor(
        private readonly color: Color,
        file: File,
        rank: Rank
    ) {
        this.position = new Position(file, rank)
    }
    abstract canMoveTo(position: Position): boolean
}

class King extends Piece {
    canMoveTo(position: Position) {
      let distance = this.position.distanceFrom(position)
      return distance.rank < 2 && distance.file < 2
    }
  }

  // Use super() to override parent calls
  // Pointing to the right instand when using a subclass

  class Set {
    has(value: number): boolean {
      // ...
    }
    add(value: number): this {
      // ...
    }
  }

  class MutableSet extends Set {
    delete(value: number): boolean {
      // ...
    }
  }