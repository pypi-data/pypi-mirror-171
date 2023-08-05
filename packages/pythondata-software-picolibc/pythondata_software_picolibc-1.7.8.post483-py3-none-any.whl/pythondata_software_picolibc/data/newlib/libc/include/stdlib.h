/*
Copyright (c) 1991, 1993
The Regents of the University of California.  All rights reserved.
c) UNIX System Laboratories, Inc.
All or some portions of this file are derived from material licensed
to the University of California by American Telephone and Telegraph
Co. or Unix System Laboratories, Inc. and are reproduced herein with
the permission of UNIX System Laboratories, Inc.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. Neither the name of the University nor the names of its contributors
may be used to endorse or promote products derived from this software
without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
 */
/*
 * stdlib.h
 *
 * Definitions for common types, variables, and functions.
 */

#ifndef _STDLIB_H_
#define _STDLIB_H_

#include <machine/ieeefp.h>
#include "_ansi.h"

#define __need_size_t
#define __need_wchar_t
#define __need_NULL
#include <stddef.h>

#include <sys/cdefs.h>
#include <machine/stdlib.h>
#ifndef __STRICT_ANSI__
#include <alloca.h>
#endif

#ifdef __CYGWIN__
#include <cygwin/stdlib.h>
#endif

#if __GNU_VISIBLE
#include <sys/_locale.h>
#endif

_BEGIN_STD_C

typedef struct
{
  int quot; /* quotient */
  int rem; /* remainder */
} div_t;

typedef struct
{
  long quot; /* quotient */
  long rem; /* remainder */
} ldiv_t;

#if __ISO_C_VISIBLE >= 1999
typedef struct
{
  long long int quot; /* quotient */
  long long int rem; /* remainder */
} lldiv_t;
#endif

#ifndef __compar_fn_t_defined
#define __compar_fn_t_defined
typedef int (*__compar_fn_t) (const void *, const void *);
#endif

#define EXIT_FAILURE 1
#define EXIT_SUCCESS 0

#define RAND_MAX __RAND_MAX

size_t	__locale_mb_cur_max (void);

#define MB_CUR_MAX __locale_mb_cur_max()

void	abort (void) _ATTRIBUTE ((__noreturn__));
int	abs (int);
#if __BSD_VISIBLE
__uint32_t arc4random (void);
__uint32_t arc4random_uniform (__uint32_t);
void    arc4random_buf (void *, size_t);
#endif
#define ATEXIT_MAX	32
int	atexit (void (*__func)(void));
double	atof (const char *__nptr);
#if __MISC_VISIBLE
float	atoff (const char *__nptr);
#endif
int	atoi (const char *__nptr);
long	atol (const char *__nptr);
void *	bsearch (const void *__key,
		       const void *__base,
		       size_t __nmemb,
		       size_t __size,
		       __compar_fn_t _compar);
void	*calloc(size_t, size_t) __malloc_like __result_use_check
	     __alloc_size2(1, 2) _NOTHROW;
div_t	div (int __numer, int __denom);
void	exit (int __status) _ATTRIBUTE ((__noreturn__));
void	free (void *) _NOTHROW;
char *  getenv (const char *__string);
#if __GNU_VISIBLE
char *  secure_getenv (const char *__string);
#endif
char *	_findenv (const char *, int *);
#if __POSIX_VISIBLE >= 200809
extern char *suboptarg;			/* getsubopt(3) external variable */
int	getsubopt (char **, char * const *, char **);
#endif
long	labs (long);
ldiv_t	ldiv (long __numer, long __denom);
void	*malloc(size_t) __malloc_like __result_use_check __alloc_size(1) _NOTHROW;
void    *valloc (size_t) __malloc_like __result_use_check __alloc_size(1) _NOTHROW;
int	mblen (const char *, size_t);
int	mbtowc (wchar_t *__restrict, const char *__restrict, size_t);
int	wctomb (char *, wchar_t);
size_t	mbstowcs (wchar_t *__restrict, const char *__restrict, size_t);
size_t	wcstombs (char *__restrict, const wchar_t *__restrict, size_t);
#if __BSD_VISIBLE || __POSIX_VISIBLE >= 200809
char *	mkdtemp (char *);
#endif
#if __GNU_VISIBLE
int	mkostemp (char *, int);
int	mkostemps (char *, int, int);
#endif
#if __MISC_VISIBLE || __POSIX_VISIBLE >= 200112 || __XSI_VISIBLE >= 4
int	mkstemp (char *);
#endif
#if __MISC_VISIBLE
int	mkstemps (char *, int);
#endif
#if __BSD_VISIBLE || (__XSI_VISIBLE >= 4 && __POSIX_VISIBLE < 200112)
char *	mktemp (char *) _ATTRIBUTE ((__deprecated__("the use of `mktemp' is dangerous; use `mkstemp' instead")));
#endif
void	qsort (void *__base, size_t __nmemb, size_t __size, __compar_fn_t _compar);
int	rand (void);
void	*realloc(void *, size_t) __result_use_check __alloc_size(2) _NOTHROW;
#if __BSD_VISIBLE
void	*reallocarray(void *, size_t, size_t) __result_use_check __alloc_size2(2, 3);
void	*reallocf(void *, size_t) __result_use_check __alloc_size(2);
#endif
#if __BSD_VISIBLE || __XSI_VISIBLE >= 4
char *	realpath (const char *__restrict path, char *__restrict resolved_path);
#endif
#if __BSD_VISIBLE
int	rpmatch (const char *response);
#endif
#if __XSI_VISIBLE
void	setkey (const char *__key);
#endif
void	srand (unsigned __seed);
double	strtod (const char *__restrict __n, char **__restrict __end_PTR);
#ifdef TINY_STDIO
int strfromd(char *__restrict str, size_t n,
	     const char *__restrict format, double fp);
#endif
#if __ISO_C_VISIBLE >= 1999
float	strtof (const char *__restrict __n, char **__restrict __end_PTR);
#ifdef TINY_STDIO
int strfromf(char *__restrict str, size_t n,
	     const char *__restrict format, float fp);
#endif
#endif
#if __MISC_VISIBLE
/* the following strtodf interface is deprecated...use strtof instead */
# ifndef strtodf
#  define strtodf strtof
# endif
#endif
long	strtol (const char *__restrict __n, char **__restrict __end_PTR, int __base);
unsigned long strtoul (const char *__restrict __n, char **__restrict __end_PTR, int __base);

#if __GNU_VISIBLE
double	strtod_l (const char *__restrict, char **__restrict, locale_t);
float	strtof_l (const char *__restrict, char **__restrict, locale_t);
#ifdef _HAVE_LONG_DOUBLE
extern long double strtold_l (const char *__restrict, char **__restrict,
			      locale_t);
#endif /* _HAVE_LONG_DOUBLE */
long	strtol_l (const char *__restrict, char **__restrict, int, locale_t);
unsigned long strtoul_l (const char *__restrict, char **__restrict, int,
			 locale_t __loc);
long long strtoll_l (const char *__restrict, char **__restrict, int, locale_t);
unsigned long long strtoull_l (const char *__restrict, char **__restrict, int,
			       locale_t __loc);
#endif

int	system (const char *__string);

#if __SVID_VISIBLE || __XSI_VISIBLE >= 4
long    a64l (const char *__input);
char *  l64a (long __input);
#endif
#if __MISC_VISIBLE
int	on_exit (void (*__func)(int, void *),void *__arg);
#endif
#if __ISO_C_VISIBLE >= 1999
void	_Exit (int __status) _ATTRIBUTE ((__noreturn__));
#endif
#if __SVID_VISIBLE || __XSI_VISIBLE
int	putenv (char *__string);
#endif
#if __BSD_VISIBLE || __POSIX_VISIBLE >= 200112
int	setenv (const char *__string, const char *__value, int __overwrite);
#endif

#if __XSI_VISIBLE >= 4
char *	gcvt (double,int,char *);
char *	gcvtf (float,int,char *);

char *	ecvt (double,int,int *,int *);
#ifdef TINY_STDIO
int	ecvt_r (double,int,int *,int *, char*, size_t);
#else
char *	ecvtbuf (double, int, int*, int*, char *);
#endif

char *	ecvtf (float,int,int *,int *);
#ifdef TINY_STDIO
int	ecvtf_r (float,int,int *,int *, char*, size_t);
#else
char *	ecvtfbuf (float, int, int*, int*, char *);
#endif

char *	fcvt (double,int,int *,int *);
#ifdef TINY_STDIO
int	fcvt_r (double, int, int*, int*, char *, size_t);
#else
char *	fcvtbuf (double, int, int*, int*, char *);
#endif

char *	fcvtf (float,int,int *,int *);
#ifdef TINY_STDIO
int	fcvtf_r (float, int, int*, int*, char *, size_t);
#else
char *	fcvtfbuf (float, int, int*, int*, char *);
#endif
#endif
char *	__itoa (int, char *, int);
char *	__utoa (unsigned, char *, int);
#if __MISC_VISIBLE
char *	itoa (int, char *, int);
char *	utoa (unsigned, char *, int);
#endif
#if __POSIX_VISIBLE
int	rand_r (unsigned *__seed);
#endif

#if __SVID_VISIBLE || __XSI_VISIBLE
struct _rand48;
double drand48 (void);
double _drand48_r (struct _rand48 *);
double erand48 (unsigned short [3]);
double _erand48_r (struct _rand48 *, unsigned short [3]);
long   jrand48 (unsigned short [3]);
long   _jrand48_r (struct _rand48 *, unsigned short [3]);
void  lcong48 (unsigned short [7]);
void  _lcong48_r (struct _rand48 *, unsigned short [7]);
long   lrand48 (void);
long   _lrand48_r (struct _rand48 *);
long   mrand48 (void);
long   _mrand48_r (struct _rand48 *);
long   nrand48 (unsigned short [3]);
long   _nrand48_r (struct _rand48 *, unsigned short [3]);
unsigned short *
       seed48 (unsigned short [3]);
unsigned short *
       _seed48_r (struct _rand48 *, unsigned short [3]);
void  srand48 (long);
void  _srand48_r (struct _rand48 *, long);
#endif /* __SVID_VISIBLE || __XSI_VISIBLE */
#if __SVID_VISIBLE || __XSI_VISIBLE >= 4 || __BSD_VISIBLE
char *	initstate (unsigned, char *, size_t);
long	random (void);
char *	setstate (char *);
void	srandom (unsigned);
#endif
#if __ISO_C_VISIBLE >= 1999
long long atoll (const char *__nptr);
#endif
#if __ISO_C_VISIBLE >= 1999
long long llabs (long long);
lldiv_t	lldiv (long long __numer, long long __denom);
long long strtoll (const char *__restrict __n, char **__restrict __end_PTR, int __base);
#endif
#if __ISO_C_VISIBLE >= 1999
unsigned long long strtoull (const char *__restrict __n, char **__restrict __end_PTR, int __base);
#endif

#ifndef __CYGWIN__
#if __MISC_VISIBLE
void	cfree (void *);
#endif
#if __BSD_VISIBLE || __POSIX_VISIBLE >= 200112
int	unsetenv (const char *__string);
#endif
#endif /* !__CYGWIN__ */

#if __POSIX_VISIBLE >= 200112
int	posix_memalign (void **, size_t, size_t) __nonnull((1))
	    __result_use_check;
#endif

char *	__dtoa (double, int, int, int *, int*, char**);
char *  __ldtoa (long double, int, int, int *, int *, char **);

void	__eprintf (const char *, const char *, unsigned int, const char *);

/* There are two common qsort_r variants.  If you request
   _BSD_SOURCE, you get the BSD version; otherwise you get the GNU
   version.  We want that #undef qsort_r will still let you
   invoke the underlying function, but that requires gcc support. */
#if __GNU_VISIBLE
void	qsort_r (void *__base, size_t __nmemb, size_t __size, int (*_compar)(const void *, const void *, void *), void *__thunk);
#elif __BSD_VISIBLE
# ifdef __GNUC__
void	qsort_r (void *__base, size_t __nmemb, size_t __size, void *__thunk, int (*_compar)(void *, const void *, const void *))
             __asm__ (__ASMNAME ("__bsd_qsort_r"));
# else
void	__bsd_qsort_r (void *__base, size_t __nmemb, size_t __size, void *__thunk, int (*_compar)(void *, const void *, const void *));
#  define qsort_r __bsd_qsort_r
# endif
#endif

/* On platforms where long double equals double.  */
#ifdef _HAVE_LONG_DOUBLE
#if __ISO_C_VISIBLE >= 1999
extern long double strtold (const char *__restrict, char **__restrict);
#endif
#endif /* _HAVE_LONG_DOUBLE */

/*
 * If we're in a mode greater than C99, expose C11 functions.
 */
#if __ISO_C_VISIBLE >= 2011
void *	aligned_alloc(size_t, size_t) __malloc_like __alloc_align(1)
	    __alloc_size(2) __result_use_check;
int	at_quick_exit(void (*)(void));
_Noreturn void
	quick_exit(int);
#endif /* __ISO_C_VISIBLE >= 2011 */

_END_STD_C

#if __SSP_FORTIFY_LEVEL > 0
#include <ssp/stdlib.h>
#endif

#endif /* _STDLIB_H_ */
