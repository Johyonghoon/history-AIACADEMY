import { createStore } from 'redux'
import todoReducer from 'todos/reducers/todo.reducer'
export const store = createStore(todoReducer)

/**
import { configureStore, 
    combineReducers, 
    getDefaultMiddleware } from "@reduxjs/toolkit"
import logger from 'redux-logger'
import todoReducer from "todos/reducers/todo.reducer"

const rootReducer = combineReducers({todoReducer})

export const store = configureStore({
    reducer: rootReducer,
    middleWare: (getDefaultMiddleware) => getDefaultMiddleware()
                                                    .concat(logger)
})
 */