/*
Copyright (c) 1990 The Regents of the University of California.
All rights reserved.

Redistribution and use in source and binary forms are permitted
provided that the above copyright notice and this paragraph are
duplicated in all such forms and that any documentation,
and/or other materials related to such
distribution and use acknowledge that the software was developed
by the University of California, Berkeley.  The name of the
University may not be used to endorse or promote products derived
from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 */
/*
FUNCTION
<<tmpfile64>>---create a large temporary file

INDEX
	tmpfile64
INDEX
	_tmpfile64_r

SYNOPSIS
	#include <stdio.h>
	FILE *tmpfile64(void);

	FILE *_tmpfile64_r(void *<[reent]>);

DESCRIPTION
Create a large temporary file (a file which will be deleted automatically),
using a name generated by <<tmpnam>>.  The temporary file is opened with
the mode <<"wb+">>, permitting you to read and write anywhere in it
as a binary file (without any data transformations the host system may
perform for text files).  The file may be larger than 2GB.

The alternate function <<_tmpfile64_r>> is a reentrant version.  The
argument <[reent]> is a pointer to a reentrancy structure.

Both <<tmpfile64>> and <<_tmpfile64_r>> are only defined if __LARGE64_FILES
is defined.

RETURNS
<<tmpfile64>> normally returns a pointer to the temporary file.  If no
temporary file could be created, the result is NULL, and <<errno>>
records the reason for failure.

PORTABILITY
<<tmpfile64>> is a glibc extension.

Supporting OS subroutines required: <<close>>, <<fstat>>, <<getpid>>,
<<isatty>>, <<lseek64>>, <<open64>>, <<read>>, <<sbrk>>, <<write>>.

<<tmpfile64>> also requires the global pointer <<environ>>.
*/

#include <stdio.h>
#include <errno.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#ifndef O_BINARY
# define O_BINARY 0
#endif

#ifdef __LARGE64_FILES

FILE *
tmpfile64 (void)
{
  FILE *fp;
  int e;
  char *f;
  char buf[L_tmpnam];
  int fd;

  do
  {
     if ((f = tmpnam (buf)) == NULL)
	return NULL;
      fd = open64 (f, O_RDWR | O_CREAT | O_EXCL | O_BINARY,
		      S_IRUSR | S_IWUSR);
  }
  while (fd < 0 && _REENT_ERRNO(ptr) == EEXIST);
  if (fd < 0)
    return NULL;
  fp = fdopen64 (fd, "wb+");
  e = _REENT_ERRNO(ptr);
  if (!fp)
    close (fd);
  (void) remove (f);
  _REENT_ERRNO(ptr) = e;
  return fp;
}

#endif /* __LARGE64_FILES */
