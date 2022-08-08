import { createBrowserHistory } from "history"
import React from "react"

export class Router extends React.Component {
    static historyContext = React.createContext({})
    history = createBrowserHistory()

    componentDidMount() {
        this.history.listen(() => this.forceUpdate())
    }

    render() {
        return (
            <Router.historyContext.Provider value={this.history}>
                {this.props.children}
            </Router.historyContext.Provider>
        )
    }
}

export class Route extends React.Component {
    render() {
        if (window.location.pathname.match(this.props.path))
            return this.props.component;
        return null;
    }
}

export class Link extends React.Component {
    static contextType = Router.historyContext
    
    handleClick = (e) => {
        e.preventDefault();
        console.log(this.context.push)
        this.context.push({pathname: this.props.to});
    }

    render() {
        return (
            <a href={this.props.to} onClick={this.handleClick}> {this.props.children} </a>
        )
    }
}