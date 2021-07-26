if (null != exc?.response)
{
  responseHeader = exc?.response?.header
  if (responseHeader?.getFirstValue("X-Frame-Options") == null)
  {
    responseHeader?.add("X-Frame-Options", "DENY")
    logger?.info("added X-Frame-Options header")
  }
}
anything()