import { useState } from "react"
import { useDispatch } from 'react-redux'
import { v4 as uuidv4 } from 'uuid'
import { addTodoAction } from '../../store/todo.reducer'

const TodoInput = () => {
    const [todo, setTodo] = useState('')
    const dispatch = useDispatch()
    const submitForm = e => {
        e.preventDefault()
        const newTodo = {
            id : uuidv4(),
            name : todo,
            complete : false
        }
        addTodo(newTodo)
        setTodo('')
    }
    const addTodo = todo => dispatch(addTodoAction(todo))
    
    const handleChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
    }
    return(<>
    <h2>스케쥴러</h2>
    <form onSubmit={submitForm} method='POST'>
    <label htmlFor="todo">할 일:</label><br/>
    <input 
        type="text" 
        id="fname" 
        name="fname"
        placeholder="할 일 입력" 
        value={todo}
        onChange={handleChange} /><br/><br/>
    </form> 
    </>)
}

export default TodoInput