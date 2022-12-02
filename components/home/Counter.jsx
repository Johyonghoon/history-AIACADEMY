import { useState } from "react"

const Counter = () => {
    const [count, setCount] = useState(0)
    return (<>
        <h1>PlusMinus</h1>
        <div>결과 값 : {count}</div>
        <button onClick={() => {setCount(count + 1)}}>
            +
        </button>
        <button onClick={() => {setCount(count - 1)}}>
            -
        </button>
    </>)
}

export default Counter