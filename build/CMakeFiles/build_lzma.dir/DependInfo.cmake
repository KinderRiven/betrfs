# The set of languages for which implicit dependencies are needed:
SET(CMAKE_DEPENDS_LANGUAGES
  )
# The set of files for implicit dependencies of each language:

# Preprocessor definitions for this target.
SET(CMAKE_TARGET_DEFINITIONS
  "_FILE_OFFSET_BITS=64"
  "_LARGEFILE64_SOURCE"
  "_SVID_SOURCE"
  "_XOPEN_SOURCE=600"
  "__LONG_LONG_SUPPORTED"
  "__STDC_FORMAT_MACROS"
  "__STDC_LIMIT_MACROS"
  )

# Targets to which this target links.
SET(CMAKE_TARGET_LINKED_INFO_FILES
  )

# The include file search paths:
SET(CMAKE_C_TARGET_INCLUDE_PATH
  "buildheader"
  "../kinclude"
  "./xz/include"
  "../include"
  "../toku_include"
  "../portability"
  ".."
  "."
  "toku_include"
  "/usr/local/include"
  )
SET(CMAKE_CXX_TARGET_INCLUDE_PATH ${CMAKE_C_TARGET_INCLUDE_PATH})
SET(CMAKE_Fortran_TARGET_INCLUDE_PATH ${CMAKE_C_TARGET_INCLUDE_PATH})
SET(CMAKE_ASM_TARGET_INCLUDE_PATH ${CMAKE_C_TARGET_INCLUDE_PATH})