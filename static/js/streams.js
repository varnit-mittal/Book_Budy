const APP_ID='4327bff84d2f4b8bab98d752f8c1aae9'
const CHANNEL='books'
const TOKEN='007eJxTYMgVLlj78yTL5y3WupxsVoLXRX252J9npYSs/dq275J83VMFBhNjI/OktDQLkxSjNJMki6TEJEuLFHNTozSLZMPExFRLB/G7KQ2BjAyLxKcyMTJAIIjPypCUn59dzMAAAP5nHqs='
let UID

const client=AgoraRTC.createClient({mode:'rtc',codec:'vp8'})

let localTracks = []
let remoteUsers= {}

let joinAndDisplayLocalStream= async()=>{

    client.on('user-published', handleUserJoined)
    client.on('user-left',handleUserLeft)

    UID=await client.join(APP_ID,CHANNEL,TOKEN,null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player=`<div class="video-container" id="user-container-${UID}">
                    <div class="username-wrapper"><span class="user-name">My Name</span></div>
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

        player=`<div class="video-container" id="user-container-${user.UID}">
                    <div class="username-wrapper"><span class="user-name">My Name</span></div>
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

joinAndDisplayLocalStream()