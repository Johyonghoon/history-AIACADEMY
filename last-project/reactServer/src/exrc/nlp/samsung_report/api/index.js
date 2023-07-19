const server = `http://localhost:8000`
const nlpService = {
    samsungReport
}
function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
}
async function samsungReport(){
    const res = await fetch(`${server}/exrc/nlp/samsung-report`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    alert('레포트 분석 ::: '+res)
    return Promise.resolve(res);
}
export default nlpService