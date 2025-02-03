/** @jsxImportSource @emotion/react */


import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { ColorModeContext, EventLoopContext } from "$/utils/context"
import { Event, getBackendURL, isTrue, refs } from "$/utils/state"
import { WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Flex as RadixThemesFlex, Link as RadixThemesLink } from "@radix-ui/themes"
import NextLink from "next/link"
import NextHead from "next/head"



export function Link_13cd27feaf87ad22aa824cd36516e4d7 () {
  
  const ref_facebook = useRef(null); refs["ref_facebook"] = ref_facebook;





  
  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} id={"facebook"} ref={ref_facebook}>

<NextLink href={"https://www.facebook.com/"} passHref={true}>

{"Facebook"}
</NextLink>
</RadixThemesLink>
  )
}

export function Toaster_6e6ebf8d7ce589d59b7d382fb7576edf () {
  
  const { resolvedColorMode } = useContext(ColorModeContext)

  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))




  
  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

export function Div_602c14884fa2de27f522fe8f94374b02 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>

<Fragment_f2f0916d2fcc08b7cdf76cec697f0750/>
</div>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Link_3b4026e4d3875554eacb8560a5acf97a () {
  
  const ref_tiktok = useRef(null); refs["ref_tiktok"] = ref_tiktok;





  
  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} id={"tiktok"} ref={ref_tiktok}>

<NextLink href={"https://www.tiktok.com/explore"} passHref={true}>

{"TikTok"}
</NextLink>
</RadixThemesLink>
  )
}

export function Fragment_f2f0916d2fcc08b7cdf76cec697f0750 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <Fragment>

{isTrue((connectErrors.length > 0)) ? (
  <Fragment>

<LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Link_053a1628d217c12bab990736f4420669 () {
  
  const ref_instagram = useRef(null); refs["ref_instagram"] = ref_instagram;





  
  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} id={"instagram"} ref={ref_instagram}>

<NextLink href={"https://www.instagram.com/"} passHref={true}>

{"Instagram"}
</NextLink>
</RadixThemesLink>
  )
}

export function Link_503ac1760e2ce60944944833532693e8 () {
  
  const ref_volver = useRef(null); refs["ref_volver"] = ref_volver;





  
  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} id={"volver"} ref={ref_volver}>

<NextLink href={"/"} passHref={true}>

{"Volver"}
</NextLink>
</RadixThemesLink>
  )
}

export default function Component() {
    




  return (
    <Fragment>

<Fragment>

<Div_602c14884fa2de27f522fe8f94374b02/>
<Toaster_6e6ebf8d7ce589d59b7d382fb7576edf/>
</Fragment>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<Link_053a1628d217c12bab990736f4420669/>
<Link_13cd27feaf87ad22aa824cd36516e4d7/>
<Link_3b4026e4d3875554eacb8560a5acf97a/>
<Link_503ac1760e2ce60944944833532693e8/>
</RadixThemesFlex>
<NextHead>

<title>

{"Reflextest | RedesSociales"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
