import { stroke } from "exrc/api"

const Stroke = () => {
    const onClick = e => {
        e.preventDefault()
        alert(`Stroke 연결 시도`)
        stroke()
    }
    return(<>
    <button onClick={onClick}>뇌졸중</button>
    </>)
}

export default Stroke