import {useState} from 'react'
import nlpService from "../api"
const SamsungReport = () => {
    const [words, setWords] = useState([])

    const onClick = e => {
        e.preventDefault()
        nlpService.samsungReport().then(res => {
            const json = JSON.parse(res)
            const arr = json['result']
            setWords(arr)
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h2>삼성 레포트 단어 개수 판독기</h2>
    <button onClick={onClick}>레포트 분석 시작</button>
    <p>버튼을 클릭하시면, 삼성 레포트의 단어 개수를 분석합니다.</p>
    <table>
        <thead>
            <tr>
            <th>단어</th><th>개수</th>
            </tr>
        </thead>
        <tbody>{words && words.map((word) => (
                <tr key={word.word}><td>{word.word}</td><td>{word.count}</td></tr>
            ))}
        </tbody>
    </table>
    </>)
}
export default SamsungReport