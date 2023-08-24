const APP_ID='4327bff84d2f4b8bab98d752f8c1aae9'
const CHANNEL=sessionStorage.getItem('room')
const TOKEN=sessionStorage.getItem('token')
const UID= Number(sessionStorage.getItem('UID'))
const user=sessionStorage.getItem('user')

const client=AgoraRTC.createClient({mode:'rtc',codec:'vp8'})

let localTracks = []
let remoteUsers= {}

let joinAndDisplayLocalStream= async()=>{

    document.getElementById('room-name').innerText=CHANNEL

    client.on('user-published', handleUserJoined)
    client.on('user-left',handleUserLeft)

    try{
        await client.join(APP_ID,CHANNEL,TOKEN,UID)
    }catch(error){
        console.log(error)
        window.open('/video/lobby','_self')
    }


    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let member= await createMember()

    let player=`<div class="video-container" id="user-container-${UID}">
                    <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                    <div class="video-player" id="user-${UID}"></div>
                </div>`

    document.getElementById('video-streams').insertAdjacentHTML('beforeend',player)

    localTracks[1].play(`user-${UID}`)

    await client.publish([localTracks[0],localTracks[1]])
}

let handleUserJoined= async(user, mediaType) =>{
    remoteUsers[user.UID]=user
    await client.subscribe(user,mediaType)

    if(mediaType==='video'){
        let player= document.getElementById(`user-container-${user.UID}`)

        if (player!=null){
            player.remove()
        }

        let member= await getMember(user)

        player=`<div class="video-container" id="user-container-${user.UID}">
                    <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                    <div class="video-player" id="user-${user.UID}"></div>
                </div>`

        document.getElementById('video-streams').insertAdjacentHTML('beforeend',player)

        user.videoTrack.play(`user-${user.UID}`)
    }

    if(mediaType==='audio'){
        user.audioTrack.play()
    }
}

let handleUserLeft= async(user) =>{
    delete remoteUsers[user.UID]
    document.getElementById(`user-container-${user.UID}`).remove()
}

let leaveAndRemoveLocalStream = async ()=>{
    for (let i=0; localTracks.length>i ;i++){
        localTracks[i].stop()
        localTracks[i].close()
    }

    await client.leave()
    deleteMember()
    window.open('/video/lobby','_self')
}

let createMember= async ()=> {
    let response= await fetch('/video/create_member/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'user':user,'uid':UID,'channelName':CHANNEL})
    })

    let member= await response.json()
    return member
}

let getMember = async(user)=>{
    let response= await fetch(`/video/get_member/?uid=${user.uid}&room_name=${CHANNEL}`)
    let member= await response.json()
    return member
}

let deleteMember= async ()=> {
    let response= await fetch('/video/delete_member/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'user':user,'uid':UID,'room_name':CHANNEL})
    })

    let member= await response.json()
}

joinAndDisplayLocalStream()

document.getElementById('leave-btn').addEventListener('click',leaveAndRemoveLocalStream)

let toggleCamera = async(e)=>{
    if(localTracks[1].muted){
        await localTracks[1].setMuted(false)
        e.target.style.backgroundColor='#D0BDF0'
    }else{
        await localTracks[1].setMuted(true)
        e.target.style.backgroundColor='red'
    }
}

document.getElementById('camera-btn').addEventListener('click',toggleCamera)

let toggleMic = async(e)=>{
    if(localTracks[0].muted){
        await localTracks[0].setMuted(false)
        e.target.style.backgroundColor='#D0BDF0'
    }else{
        await localTracks[0].setMuted(true)
        e.target.style.backgroundColor='red'
    }
}

document.getElementById('mic-btn').addEventListener('click',toggleMic)
window.addEventListener('beforeunload',deleteMember)