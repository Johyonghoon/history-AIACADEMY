import axios from "axios";
import { setMaxListeners } from "events";
import { useEffect, useState } from "react";
import Pagination from "./admin/Pagination";

export default function Home(){
    const [list, setList] = useState([])
    const [rows, setRows] = useState<number[]>([])
    const [pages, setPages] = useState<number[]>([])
    const [rowCnt, setRowCnt] = useState(0)
    const [requestPage, setRequestPage] = useState(0)
    const [startRowPerPage, setStartRowPerPage] = useState(0)
    const [endRowPerPage, setEndRowPerPage] = useState(0)
    const [startPagePerBlock, setstartPagePerBlock] = useState(0)
    const [endPagePerBlock, setEndPagePerBlock] = useState(0)
    const [prevArrow, setPrevArrow] = useState(false)
    const [nextArrow, setNextArrow] = useState(false)
    
    useEffect(()=>{
        axios
        .get('http://localhost:8000/users/page/1')
        .then(res => {
            setRowCnt(Number(res.data.pager.row_cnt))
            setStartRowPerPage(Number(res.data.pager.start_row_per_page))
            setEndRowPerPage(Number(res.data.pager.end_row_per_page))
            setstartPagePerBlock(Number(res.data.pager.start_page_per_block))
            setEndPagePerBlock(Number(res.data.pager.end_page_per_block))
            setRequestPage(Number(res.data.pager.request_page))
            setList(res.data.users.items)
            console.log(" ### 페이지 내용 표시 ### ")
            let rows: number[] = []
            let pages: number[] = []
            for(let i =startRowPerPage; i <= endRowPerPage; i++){
                rows.push(i)
            }
            setRows(rows)
            console.log(" ### 블록 내용 표시 ### ")
            for(let i =startPagePerBlock; i <= endPagePerBlock; i++){
              pages.push(i)
          }
          setPages(pages)
          setPrevArrow(res.data.pager.prev_arrow)
          setNextArrow(res.data.pager.next_arrow)
          console.log(` 사용자가 요청한 페이지 번호: ${requestPage}`)
        })
        .catch(err => {console.log(err)})
    }, [])

    return (
        <>
        <h2> 회원목록 </h2>
        <h6> 회원수: {rowCnt} </h6>
        <h6></h6>
        <h6></h6>
        <h6></h6>
        <table>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>비번</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
                </tr>
            </thead>
            <tbody>
                {prevArrow && <span> 이전 </span>}
                {list && list.map(({user_id, user_email, user_name, phone, birth, address, job, user_interests})=>(
                    <tr key={user_id}>
                        <td>{user_id}</td><td>{user_email}</td><td>{user_name}</td>
                        <td>{phone}</td><td>{birth}</td><td>{address}</td>
                        <td>{job}</td><td>{user_interests}</td>
                    </tr>
                ))}
            </tbody>
        </table>
        <div className="page-container">
            {rows && rows.map((v, i) => (<span style={{"border": "1px solid black"}}>{v+1}</span>))}
            {nextArrow && <span> 이후 </span>}
        </div>
        </>
      
    );
}