import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection
} from "streamlit-component-lib";
import React, { useEffect, useRef } from "react"

import iframeResize from "iframe-resizer/js/iframeResizer"
import raw from "raw.macro"

interface ProfileReportProps extends ComponentProps {
  args: {
    html: string
  }
}

const IFRAME_RESIZER_AGENT = document.createElement("script")
IFRAME_RESIZER_AGENT.type = "text/javascript"
IFRAME_RESIZER_AGENT.async = true
IFRAME_RESIZER_AGENT.innerHTML = raw("iframe-resizer/js/iframeResizer.contentWindow")

const insertIFrameResizerAgent = (content: string) => {
  // Load HTML string as DOM element
  const container = document.createElement("html")
  container.innerHTML = content

  // Remove Profile Report navbar as navigation does not work
  container.querySelector("nav")?.remove()

  // Create a new tab when you click a link
  container.querySelectorAll("a").forEach((element: HTMLAnchorElement) => {
    element.target = "_blank"
  })

  // Append IFrame Resizer contentWindow script
  container.querySelector("head")?.appendChild(IFRAME_RESIZER_AGENT)

  return container.innerHTML
}

const ProfileReport = ({ args }: ProfileReportProps) => {
  const iframeRef = useRef(null)

  useEffect(() => {
    if (iframeRef.current !== null) {
      iframeResize({
          onResized: ({ height }: { height: number }) => {
            Streamlit.setFrameHeight(height) 
          }
        },
        iframeRef.current
      )
    }
  })

  return (
    <iframe
      ref={iframeRef}
      title="Profile Report"
      width="100%"
      srcDoc={insertIFrameResizerAgent(args.html)}
      frameBorder={0}
      seamless>
    </iframe>
  )
}

export default withStreamlitConnection(ProfileReport)
