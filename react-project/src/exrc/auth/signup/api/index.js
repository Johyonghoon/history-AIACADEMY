const server = `http://localhost:8000`
const signupService = {
    apiSignUp
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
async function apiSignUp(){
    const res = await fetch(`${server}/exrc/auth/signup`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    alert('더미 사용자 생성 ::: '+res)
    return Promise.resolve(res);
}
export default signupService