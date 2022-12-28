import 'todos/styles/TodoList.css'
import { deleteTodoAction, toggleTodoAction } from 'todos/reducers/todo.reducer'
import { useDispatch, useSelector } from 'react-redux'

const TodoList = () => {
    const todos = useSelector(state => state.todos)
    const dispatch = useDispatch()
    const toggleTodo = id => dispatch(toggleTodoAction(id))
    const deleteTodo = id => dispatch(deleteTodoAction(id))
    return(<>
    <h2>할일 목록</h2>
    <table className='table'>
    <thead>
        <tr>
            <th>Todo List</th>   
        </tr>
    </thead>
    <tbody>
        { todos.length === 0 && (<tr>
            <td>등록된 할 일이 없습니다.</td>  
        </tr>)}
        { todos.length !== 0 && todos.map( todo => (<tr key={todo.id}>
            <td><input type="checkbox" checked={todo.complete} 
            onChange={toggleTodo.bind(null, todo.id)}/>{ todo.complete 
                        ? <span style={{textDecoration: "line-through"}}>{todo.name}</span> 
                        : <span>{todo.name}</span>}
                <button onClick={deleteTodo.bind(null, todo.id)}>X</button>
            </td>  
            
        </tr>))}
    </tbody>
    </table>
    </>)
}

export default TodoList