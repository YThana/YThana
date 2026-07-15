import Vision
import AppKit
import CoreImage

let args = CommandLine.arguments
let inputURL = URL(fileURLWithPath: args[1])
let outputURL = URL(fileURLWithPath: args[2])

guard let ciImage = CIImage(contentsOf: inputURL) else { fatalError("cannot load image") }
let request = VNGenerateForegroundInstanceMaskRequest()
let handler = VNImageRequestHandler(ciImage: ciImage)
try handler.perform([request])
guard let result = request.results?.first else { fatalError("no subject found") }
let maskedBuffer = try result.generateMaskedImage(ofInstances: result.allInstances, from: handler, croppedToInstancesExtent: false)
let masked = CIImage(cvPixelBuffer: maskedBuffer)
let ctx = CIContext()
guard let cg = ctx.createCGImage(masked, from: masked.extent) else { fatalError("render fail") }
let rep = NSBitmapImageRep(cgImage: cg)
try rep.representation(using: .png, properties: [:])!.write(to: outputURL)
print("ok")
