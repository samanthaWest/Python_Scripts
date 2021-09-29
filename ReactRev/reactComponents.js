// Pure Components and Regular Components

import React, { useState, useEffect } from 'react';

// Regular Component
class Greeting extends React.Component {
    render() {
        return <h1>Hello, {this.props.name}</h1>
    }
}

// Pure React Component
class Greeting2 extends React.PureComponent {
    render() {
        return <div>hi</div>
    }
}

// The difference btw a regular and pure component is that React.Component does not implement
// shouldComponentUpdate(). But React.PureComponent implements it with a shallow prop and 
// state comparison. Becaue PureComponent only compares shallow objects, if they contain complex
// DS then it can provide false negatives. Only use Pure Component when you have shallow updates wiith simple props and states.

// Deeper Dive into React Component ::
// The only method you need to define if you extend React.Component is render()

// LifeCycle
// Mounting
//  - constructor: called before component is mounted, used for init local state or binding event handler methods to an instance
// constructor is the ohnly place you should assign this.state directly. 

class Test1 extends React.Component {
    constructor(props){
        super(props);
        this.state = { counter: 0 };
        this.handleClick = this.handleClick.bind(this);
    }
}

//  render: can let you return react elements, arrays and frafments, portals, strings and numbers or null (nothing)
// anything in  render should be pure and only change based off state. If you need to interact with the browser use another lifecycle method.

class Test2 extends React.Component {
    constructor(props) {
        super(props);
        this.state = 'test'
    }

    render () {
        <div> testing </div>
    }
}

// componentDidMount() : invoked immeditalty after component is mounted (inserted into tree). Initializations that require DOM nodes should be here.
// If you need to load data from a remote endpoint, this would be a good place for the network request. This method
// is also a good place to set up any subscriptions and you need to unsub in componentWillUnmount()
// You can call setState here which will cause a double re-render but can be used if you need to gaurentee that
// the user won't see the init state. This pattern would cause performance issues though. In most cases
// assign init state in the constructor instead. But it can be used for cases like modals or tooltips where you need to measure the DOM node
// before rendering something based on size and position.

class Test3 extends React.Component {

    componentDidMount() {
        console.log("Elements rendered on the DOM Tree and component mounted. ");
    }

    render () {
        <div> Test</div>
    }
}

// Updating any updates causes by changes in props or state thse methods will be call in the follow order when comp is being re-rendered. render() -> componentDidUpdate()

// componentDidUpdate: invoked immeditatly after updating occurs. This element is not called on the init render. You can use this to operate on
// the DOM after component has been updated. This is a  good place to do network requests as long as you compare them
// to the previous props.

class Test4 extends React.Component {
    componentDidUpdate(prevProps) {
        // Typical usage is comparing previous w/ current props
        console.log(prevProps);
    }

    render () {
        <div>Test </div>
    }
}

// Un- Mounting
//  componentWillUnmount :  called after component is unmounted and destroyed. Perform any cleanup here Such as invalidating times, cancelling network requests or
// cleaning up any subscriptions that where creatign in componentDidMount(). Do not call state in componetWillUnmount() because the component
// will never be re-rendered. Once it is unmounted it will never mount again.

class Test5 extends React.Component {
    componentWillUnMount() {
        console.log('un mounting');
    }
    render() {
        <div> unmounting </div>
    }
}


// ForceUpdate() : If your render method depends on some other data, then you can tell React that the component needs re-rendering.
// This will force render() to be called skipping passed shouldComponentUpdate(). Normally you should avoid this and only read from
// this.props and this.state in render

// SetState() enqueue changes to component state. This tells React the component and it's children need to be re-rendered. Think of it
// as a req vs an immediate update. React may delay it it does not gaurentee the state changes will apply immediatly.
// This makes reading this.state right after calling setState() a potential pitfal. Use componentDidUpdate or setState callback which guarentee to fire after the update 
// has been applied. Set state will always do a re-render unlesss shouldComponentUpdate() return false.

// No matter how many statecalls in a react handler they will produce only one re-render at the end of the event.
// This is crucial for good performance in large apps. 
// https://stackoverflow.com/questions/48563650/does-react-keep-the-order-for-state-updates/48610973#48610973 
// https://github.com/facebook/react/issues/11527#issuecomment-360199710

class Test6 extends React.Component {
    // Using an updator function for setState
    testing = (newItem) => {
        this.setState((state, props) => {
            return { counter: state.counter + props.step };
        });

        // SHalow merge
        this.setState({ quantity: 1 });
    }
}

// UseState - store state in functions

function Counter({initialCount}) {
    const [count, setCount] = useState(initialCount);

    return (
        <>
        Count: {count}
        <button onClick={ () => setCount(initialCount)}>Reset</button>
        <button onClick={() => setCount(prevCount => prevCount - 1)}>-</button>
        <button onClick={() => setCount(prevCount => prevCount + 1)}>+</button>
        </>
    );
}

// Alternativley

function Counter2() {
    const [state, setState] = useState({})
    setState(prevState => {
        return {...prevState, ...updateValues};
    });
}

// But if your going to be using setState to manage objects you might as well use the reducer method

// Can return a state with an initial computation
function Counter3() {
    // That will only be executed on the initial render
    const [state, setState] = useState(() => {
        const initialState = someExpensiveComputation(props);
        return initialState;
    })
}

// UseEffect - will run after render is commitedo nto screen. You can choose to fire them
// only when certain values have changed. Often effects created resources need to be cleaned up before component leaves. to do this
// the function passed to useEffect may return a clean up function. The clean up func runs before component is removed from
// the UI to prevent any memory leaks.
// If using this make sure to include all values from component scope such as props and state or else the code will ref stale values
// that could;ve changed over time from previous renders.

function Counter4() {

    useEffect( () => {
        console.log('testing effect')
    }, [props.source]); // you can pass an empty array as the second args this tells react you efect do not re-render
}

// https://reactjs.org/docs/hooks-reference.html#usestate
// Using Context

const themes = {
    light : {
        foreground: "#000",
        background: "#FFF"
    }
}

const ThemeContext = React.createContext(themes.light)

function App() {
    return (
        <ThemeContext.Provider value={themes.light}>
            <Toolbar></Toolbar>
        </ThemeContext.Provider>
    );
}

function Toolbar(props) {
    return(
        <div>
            <ThemedButton></ThemedButton>
        </div>
    );
}

function ThemedButton() {
    const theme = useContext(ThemeContext);
    return (
        <button> style=:{{ backgroundColor: theme.background }} Click me im styled! </button>
    )
}

// Using Reducer - alt to usestate when you have more complex objects. Helps you opt performance for comp that trigger deep updates because you can pass dispatch down instead of callbacks.

const initialState = {count: 0};

function reducer(state, action) {
    switch (action.type) {
        case 'increment':
            return { count: state.count + 1 }
        case 'decrement':
            return { count: state.count -1 };
        default:
            throw new Error();
    }
}

function Counter() {
    const [state, dispatch] = useReducer(reducer, initialState);
    return (
        <>
        Count: {state.count}
      <button onClick={() => dispatch({type: 'decrement'})}>-</button>
      <button onClick={() => dispatch({type: 'increment'})}>+</button>
        </>
    )
}

