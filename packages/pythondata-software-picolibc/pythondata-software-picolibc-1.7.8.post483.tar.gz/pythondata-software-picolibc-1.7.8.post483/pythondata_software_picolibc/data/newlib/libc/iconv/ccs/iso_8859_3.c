/*
 * This file was generated automatically - don't edit it.
 * File contains iconv CCS tables for iso_8859_3 encoding.
 */

#include "ccsbi.h"

#if defined (ICONV_TO_UCS_CCS_ISO_8859_3) \
 || defined (ICONV_FROM_UCS_CCS_ISO_8859_3)

#include <_ansi.h>
#include <sys/types.h>
#include <sys/param.h>
#include "ccs.h"
#include "ccsnames.h"

#if (BYTE_ORDER == LITTLE_ENDIAN)
#  define W(word) (word) & 0xFF, (word) >> 8
#elif (BYTE_ORDER == BIG_ENDIAN)
#  define W(word) (word) >> 8, (word) & 0xFF
#else
#  error "Unknown byte order."
#endif

/*
 * 8-bit iso_8859_3 -> UCS table (512 bytes).
 * ======================================================================
 */
#if defined (ICONV_TO_UCS_CCS_ISO_8859_3)

static const __uint16_t
to_ucs_speed_iso_8859_3[] =
{
	0x0000,0x0001,0x0002,0x0003,0x0004,0x0005,0x0006,0x0007,
	0x0008,0x0009,0x000A,0x000B,0x000C,0x000D,0x000E,0x000F,
	0x0010,0x0011,0x0012,0x0013,0x0014,0x0015,0x0016,0x0017,
	0x0018,0x0019,0x001A,0x001B,0x001C,0x001D,0x001E,0x001F,
	0x0020,0x0021,0x0022,0x0023,0x0024,0x0025,0x0026,0x0027,
	0x0028,0x0029,0x002A,0x002B,0x002C,0x002D,0x002E,0x002F,
	0x0030,0x0031,0x0032,0x0033,0x0034,0x0035,0x0036,0x0037,
	0x0038,0x0039,0x003A,0x003B,0x003C,0x003D,0x003E,0x003F,
	0x0040,0x0041,0x0042,0x0043,0x0044,0x0045,0x0046,0x0047,
	0x0048,0x0049,0x004A,0x004B,0x004C,0x004D,0x004E,0x004F,
	0x0050,0x0051,0x0052,0x0053,0x0054,0x0055,0x0056,0x0057,
	0x0058,0x0059,0x005A,0x005B,0x005C,0x005D,0x005E,0x005F,
	0x0060,0x0061,0x0062,0x0063,0x0064,0x0065,0x0066,0x0067,
	0x0068,0x0069,0x006A,0x006B,0x006C,0x006D,0x006E,0x006F,
	0x0070,0x0071,0x0072,0x0073,0x0074,0x0075,0x0076,0x0077,
	0x0078,0x0079,0x007A,0x007B,0x007C,0x007D,0x007E,0x007F,
	0x0080,0x0081,0x0082,0x0083,0x0084,0x0085,0x0086,0x0087,
	0x0088,0x0089,0x008A,0x008B,0x008C,0x008D,0x008E,0x008F,
	0x0090,0x0091,0x0092,0x0093,0x0094,0x0095,0x0096,0x0097,
	0x0098,0x0099,0x009A,0x009B,0x009C,0x009D,0x009E,0x009F,
	0x00A0,0x0126,0x02D8,0x00A3,0x00A4,INVALC,0x0124,0x00A7,
	0x00A8,0x0130,0x015E,0x011E,0x0134,0x00AD,INVALC,0x017B,
	0x00B0,0x0127,0x00B2,0x00B3,0x00B4,0x00B5,0x0125,0x00B7,
	0x00B8,0x0131,0x015F,0x011F,0x0135,0x00BD,INVALC,0x017C,
	0x00C0,0x00C1,0x00C2,INVALC,0x00C4,0x010A,0x0108,0x00C7,
	0x00C8,0x00C9,0x00CA,0x00CB,0x00CC,0x00CD,0x00CE,0x00CF,
	INVALC,0x00D1,0x00D2,0x00D3,0x00D4,0x0120,0x00D6,0x00D7,
	0x011C,0x00D9,0x00DA,0x00DB,0x00DC,0x016C,0x015C,0x00DF,
	0x00E0,0x00E1,0x00E2,INVALC,0x00E4,0x010B,0x0109,0x00E7,
	0x00E8,0x00E9,0x00EA,0x00EB,0x00EC,0x00ED,0x00EE,0x00EF,
	INVALC,0x00F1,0x00F2,0x00F3,0x00F4,0x0121,0x00F6,0x00F7,
	0x011D,0x00F9,0x00FA,0x00FB,0x00FC,0x016D,0x015D,0x02D9,
	
};

#endif /* ICONV_TO_UCS_CCS_ISO_8859_3 */

/*
 * 8-bit UCS -> iso_8859_3 speed-optimized table (1282 bytes).
 * ======================================================================
 */

#if defined (ICONV_FROM_UCS_CCS_ISO_8859_3)

static const unsigned char
from_ucs_speed_iso_8859_3[] =
{
	W(0x02D9), /* Real 0xFF mapping. 0xFF is used to mark invalid codes */
	/* Heading Block */
	W(0x0202),W(0x0302),W(0x0402),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	W(INVBLK),W(INVBLK),W(INVBLK),W(INVBLK),
	/* Block 1, Array index 0x0202 */
	0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,
	0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,
	0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,
	0x18,0x19,0x1A,0x1B,0x1C,0x1D,0x1E,0x1F,
	0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,
	0x28,0x29,0x2A,0x2B,0x2C,0x2D,0x2E,0x2F,
	0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,
	0x38,0x39,0x3A,0x3B,0x3C,0x3D,0x3E,0x3F,
	0x40,0x41,0x42,0x43,0x44,0x45,0x46,0x47,
	0x48,0x49,0x4A,0x4B,0x4C,0x4D,0x4E,0x4F,
	0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,
	0x58,0x59,0x5A,0x5B,0x5C,0x5D,0x5E,0x5F,
	0x60,0x61,0x62,0x63,0x64,0x65,0x66,0x67,
	0x68,0x69,0x6A,0x6B,0x6C,0x6D,0x6E,0x6F,
	0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,
	0x78,0x79,0x7A,0x7B,0x7C,0x7D,0x7E,0x7F,
	0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87,
	0x88,0x89,0x8A,0x8B,0x8C,0x8D,0x8E,0x8F,
	0x90,0x91,0x92,0x93,0x94,0x95,0x96,0x97,
	0x98,0x99,0x9A,0x9B,0x9C,0x9D,0x9E,0x9F,
	0xA0,0xFF,0xFF,0xA3,0xA4,0xFF,0xFF,0xA7,
	0xA8,0xFF,0xFF,0xFF,0xFF,0xAD,0xFF,0xFF,
	0xB0,0xFF,0xB2,0xB3,0xB4,0xB5,0xFF,0xB7,
	0xB8,0xFF,0xFF,0xFF,0xFF,0xBD,0xFF,0xFF,
	0xC0,0xC1,0xC2,0xFF,0xC4,0xFF,0xFF,0xC7,
	0xC8,0xC9,0xCA,0xCB,0xCC,0xCD,0xCE,0xCF,
	0xFF,0xD1,0xD2,0xD3,0xD4,0xFF,0xD6,0xD7,
	0xFF,0xD9,0xDA,0xDB,0xDC,0xFF,0xFF,0xDF,
	0xE0,0xE1,0xE2,0xFF,0xE4,0xFF,0xFF,0xE7,
	0xE8,0xE9,0xEA,0xEB,0xEC,0xED,0xEE,0xEF,
	0xFF,0xF1,0xF2,0xF3,0xF4,0xFF,0xF6,0xF7,
	0xFF,0xF9,0xFA,0xFB,0xFC,0xFF,0xFF,0xFF,
	/* Block 2, Array index 0x0302 */
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xC6,0xE6,0xC5,0xE5,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xD8,0xF8,0xAB,0xBB,
	0xD5,0xF5,0xFF,0xFF,0xA6,0xB6,0xA1,0xB1,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xA9,0xB9,0xFF,0xFF,0xAC,0xBC,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xDE,0xFE,0xAA,0xBA,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xDD,0xFD,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xAF,0xBF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	/* Block 3, Array index 0x0402 */
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xA2,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
	0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
};

#endif /* ICONV_FROM_UCS_CCS_ISO_8859_3 */

/*
 * iso_8859_3 CCS description table.
 * ======================================================================
 */
const iconv_ccs_t
_iconv_ccs_iso_8859_3 =
{
	TABLE_VERSION_1, /* Table version */
	ICONV_CCS_ISO_8859_3, /* CCS name */
	TABLE_8BIT, /* Table bits */
	0, /* Not Used */
#if defined (ICONV_FROM_UCS_CCS_ISO_8859_3)
	(__uint16_t *)&from_ucs_speed_iso_8859_3, /* UCS -> iso_8859_3 table */
#else
	(__uint16_t *)NULL,
#endif
	0, /* Not Used */
#if defined (ICONV_TO_UCS_CCS_ISO_8859_3)
	(__uint16_t *)&to_ucs_speed_iso_8859_3 /* iso_8859_3 -> UCS table */
#else
	(__uint16_t *)NULL,
#endif
};

#endif /* ICONV_TO_UCS_CCS_ISO_8859_3) || ... */

