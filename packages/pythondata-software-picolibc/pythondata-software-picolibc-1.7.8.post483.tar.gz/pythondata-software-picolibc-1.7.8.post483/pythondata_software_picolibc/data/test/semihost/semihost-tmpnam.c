/*
 * SPDX-License-Identifier: BSD-3-Clause
 *
 * Copyright © 2020 Keith Packard
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *
 * 3. Neither the name of the copyright holder nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <stdlib.h>
#include <limits.h>
#include <semihost.h>

int
main(void)
{
	int	ret = 0;
	char	pathname[PATH_MAX];
	int	identifier;
	int	fd;

	for (identifier = 0; identifier <= 255; identifier++) {
		ret = sys_semihost_tmpnam(pathname, identifier, PATH_MAX);
		if (ret == 0)
			break;
	}
	if (ret != 0) {
		printf("tmpnam fails, ret %d, errno %d\n", ret, sys_semihost_errno());
		exit(1);
	}
	printf("using tmpname \"%s\"\n", pathname);
	fd = sys_semihost_open(pathname, 4);
	if (fd < -1) {
		printf("open fails, ret %d errno %d\n", fd, sys_semihost_errno());
		exit(2);
	}
	ret = sys_semihost_close(fd);
	if (ret != 0) {
		printf("close fails, ret %d errno %d\n", ret, sys_semihost_errno());
		exit(3);
	}
	ret = sys_semihost_remove(pathname);
	if (ret != 0) {
		printf("remove fails, ret %d, errno %d\n", ret, sys_semihost_errno());
		exit(4);
	}
	exit(0);
}
