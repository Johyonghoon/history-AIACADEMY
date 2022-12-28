

const initialState = { todos: [], todo: {} }

export const addTodoAction = todo => ({type: "ADD_TODO", payload: todo})
export const toggleTodoAction = todoId => ({type: "TOGGLE_TODO", payload: todoId})
export const deleteTodoAction = todoId => ({type: "DELETE_TODO", payload: todoId})


const todoReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'ADD_TODO':
        return {...state, todos: [...state.todos, action.payload]}
      case 'TOGGLE_TODO':
        return {...state, todos: state.todos.map(
          todo => (todo.id === action.payload) ? {...todo, complete: !todo.complete} : todo)}
      case 'DELETE_TODO':
        return {...state, todos: state.todos.filter(todo => todo.id !== action.payload)}
      default:
        return state
    }
} 

export default todoReducer

/**

const todoSlice = createSlice({
  name: 'todos',
  initialState: {
    todoState: {id: '', name: '', complete: False},
    todosState: [],
    type: '',
    keyword: '',
    params: {}
  },
  reducers : {
    [addTodo.fulfilled]: ( state, action ) => {
      state.todoState = action.payload
    },
    [toggleTodo.fulfilled]: state.todos.map( todo => (todo.id === action.payload) ? {...todo, complete: !todo.complete state, action ) => {},
    [deleteTodo.fulfilled]: ( state, action ) => {},
  }
})
 */