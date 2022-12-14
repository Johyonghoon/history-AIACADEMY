import { stroke } from "exrc/api"

const Stroke = () => {
    const onClick = e => {
        e.preventDefault()
        alert(`Stroke 연결 시도`)
        stroke()
        .then(() => {
            alert(`Stroke 연결 성공`)
        })
    }
    return(<>
    <button onClick={onClick}>뇌졸중</button>
    </>)
}

export default Stroke