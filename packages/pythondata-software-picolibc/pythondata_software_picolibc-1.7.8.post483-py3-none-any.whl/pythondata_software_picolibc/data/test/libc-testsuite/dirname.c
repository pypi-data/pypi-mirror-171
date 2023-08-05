/*
 * Copyright © 2005-2020 Rich Felker
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
 * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <libgen.h>
#include <stdlib.h>

#define TEST(p, b) do {                                                 \
        tmp = strdup((p));                                              \
        s = dirname (tmp);                                              \
        if (strcmp((b),s)) {                                            \
            printf(__FILE__ ":%d: dirname(\"%s\") returned \"%s\"; expected \"%s\"\n", \
                   __LINE__, (p), s, (b));                              \
            err++;                                                      \
        }                                                               \
        free(tmp);                                                      \
    } while (0)

int test_dirname(void)
{
	char *tmp, *s;
	int err=0;

	if (strcmp(dirname(NULL), ".")) {
		printf(__FILE__ ":%d: dirname(NULL) returned \"%s\"; "
			"expected \".\"\n", __LINE__, dirname(NULL));
		err++;
	}
	TEST("", ".");
	TEST("/usr/lib", "/usr");
	TEST("/usr/", "/");
	TEST("usr", ".");
	TEST("/", "/");
	TEST("///", "/");
	TEST(".", ".");
	TEST("..", ".");

	return err;
}

#undef dirname
#define TEST_NAME dirname
#include "testcase.h"
