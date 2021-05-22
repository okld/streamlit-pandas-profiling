import { useEffect, useState } from "react"
import { ComponentProps, Streamlit, withStreamlitConnection } from "streamlit-component-lib";

// eslint-disable-next-line import/no-webpack-loader-syntax
import iframeResizerAgentSource from "!!raw-loader!iframe-resizer/js/iframeResizer.contentWindow"
import iframeResizer from "iframe-resizer/js/iframeResizer"

interface ProfileReportProps extends ComponentProps {
  args: {
    html: string
    height: number
  }
}

const iframeResizerAgent = document.createElement("script")
iframeResizerAgent.innerHTML = iframeResizerAgentSource
iframeResizerAgent.type = "text/javascript"
iframeResizerAgent.async = true

const handleHeight = ({ height }: any) => {
  Streamlit.setFrameHeight(height)
}
 
const ProfileReport = ({ args }: ProfileReportProps) => {
  const [html, setHtml] = useState("") 

  useEffect(() => {
    const fixedHeightProps = (args.height === null) ? {} : {
      maxHeight: args.height,
      scrolling: true,
      autoResize: false
    }

    const iframe = iframeResizer({
      checkOrigin: false,
      onResized: handleHeight,
      ...fixedHeightProps,
    }, "#iframe-profile-report")

    return () => {
      iframe.close()
    }
  }, [args.height])

  useEffect(() => {
    const container = document.createElement("html")
    container.innerHTML = args.html

    container.querySelector("head")?.appendChild(iframeResizerAgent)
    container.querySelectorAll("a").forEach((element: HTMLAnchorElement) => {
      element.target = "_blank"
    })

    setHtml(container.innerHTML)
    container.remove()
  }, [args.html])

  return (
    <iframe
      id="iframe-profile-report"
      title="Profile Report"
      width="100%"
      frameBorder={0}
      srcDoc={html}
    />
  )
}

export default withStreamlitConnection(ProfileReport)
