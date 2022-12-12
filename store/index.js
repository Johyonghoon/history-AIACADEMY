import { createStore } from 'redux'
import todoReducer from 'todos/reducers/todo.reducer'
export const store = createStore(todoReducer)
